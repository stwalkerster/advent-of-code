BORDER_NORTH = 0
BORDER_EAST = 1
BORDER_SOUTH = 2
BORDER_WEST = 3

class Plot:
    def count_borders(self) -> int:
        return sum([1 for x in self.borders if x])

    def __init__(self, crop):
        self.crop = crop
        self.borders = [True, True, True, True]
        self.borders_visited = [False, False, False, False]
        self.region = None

    def __repr__(self):
        border_count = self.count_borders()

        return f'[ {self.crop} {self.region} {border_count} ]'


class Region:
    def __init__(self, region):
        self.region = region
        self.borders = 0
        self.sides = 0
        self.area = 0

    def __repr__(self):
        return f'{self.region} => {self.area}m2 / {self.borders}m; {self.sides} sides'

    def cost(self):
        return self.area * self.borders

    def discounted_cost(self):
        return self.area * self.sides


def flood_fill(data, x, y, region, meta):
    if data[y][x].region is not None:
        return

    data[y][x].region = region
    borders = 0
    meta[region].area += 1

    # north
    if (y - 1) >= 0 and data[y - 1][x].crop == data[y][x].crop:
        flood_fill(data, x, y - 1, region, meta)
        borders -= 1
        data[y][x].borders[BORDER_NORTH] = False
        data[y][x].borders_visited[BORDER_NORTH] = True

    # east
    if (x + 1) < len(data[y]) and data[y][x + 1].crop == data[y][x].crop:
        flood_fill(data, x + 1, y, region, meta)
        borders -= 1
        data[y][x].borders[BORDER_EAST] = False
        data[y][x].borders_visited[BORDER_EAST] = True

    # south
    if (y + 1) < len(data) and data[y + 1][x].crop == data[y][x].crop:
        flood_fill(data, x, y + 1, region, meta)
        borders -= 1
        data[y][x].borders[BORDER_SOUTH] = False
        data[y][x].borders_visited[BORDER_SOUTH] = True

    # west
    if (x - 1) >= 0 and data[y][x - 1].crop == data[y][x].crop:
        flood_fill(data, x - 1, y, region, meta)
        borders -= 1
        data[y][x].borders[BORDER_WEST] = False
        data[y][x].borders_visited[BORDER_WEST] = True

    meta[region].borders += 4 + borders


def part1(input_file):
    meta, data = load_model(input_file)

    return sum([meta[y].cost() for y in meta])


def load_model(input_file):
    data = [
        [Plot(x) for x in list(line)]
        for line in open(input_file).read().split('\n')
        if line != ""
    ]

    last_region = -1
    meta = dict()
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x].region is not None:
                continue

            last_region += 1
            meta[last_region] = Region(last_region)
            flood_fill(data, x, y, last_region, meta)

    return meta, data


def part2(input_file):
    meta, data = load_model(input_file)

    # iterate y, x
    # iterate unvisited borders
    # follow border:
    #   check for connecting borders
    #   if so, it's a direction change
    #   check for continuing border in next plot
    #   check next plot is part of same region

    for y in range(len(data)):
        for x in range(len(data[y])):
            for border in [BORDER_NORTH, BORDER_EAST, BORDER_SOUTH, BORDER_WEST]:
                if not data[y][x].borders[border]:
                    continue
                if data[y][x].borders_visited[border]:
                    continue

                data[y][x].borders_visited[border] = True
                meta[data[y][x].region].sides += 1

                if border in [BORDER_EAST, BORDER_WEST]:
                    for y1 in range(y, len(data)):
                        if data[y][x].region != data[y1][x].region:
                            break
                        if data[y1][x].borders[border]:
                            data[y1][x].borders_visited[border] = True
                        else:
                            break

                if border in [BORDER_NORTH, BORDER_SOUTH]:
                    for x1 in range(x + 1, len(data[y])):
                        if data[y][x].region != data[y][x1].region:
                            break
                        if data[y][x1].borders[border]:
                            data[y][x1].borders_visited[border] = True
                        else:
                            break

    return sum([meta[y].discounted_cost() for y in meta])


if __name__ == '__main__':
    print(part2("input.txt"))
