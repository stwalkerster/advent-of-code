class Plot:
    region = None
    borders = 4

    def __init__(self, crop):
        self.crop = crop
    def __str__(self):
        return f'[ {self.crop} {self.region} {self.borders} ]'


class Region:
    borders = 0
    area = 0

    def __init__(self, region):
        self.region = region
    def __repr__(self):
        return f'{self.region} => {self.area}m2 / {self.borders}m'

    def cost(self):
        return self.area * self.borders


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
    # east
    if (x + 1) < len(data[y]) and data[y][x + 1].crop == data[y][x].crop:
        flood_fill(data, x + 1, y, region, meta)
        borders -= 1
    # south
    if (y + 1) < len(data) and data[y + 1][x].crop == data[y][x].crop:
        flood_fill(data, x, y + 1, region, meta)
        borders -= 1
    # west
    if (x - 1) >= 0 and data[y][x - 1].crop == data[y][x].crop:
        flood_fill(data, x - 1, y, region, meta)
        borders -= 1

    data[y][x].borders += borders
    meta[region].borders += data[y][x].borders


def part1(input_file):
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

    return sum([meta[y].cost() for y in meta])

def part2(input_file):
    data = [line for line in open(input_file).read().split('\n') if line != ""]

    return None


if __name__ == '__main__':
    part1("input.txt")
