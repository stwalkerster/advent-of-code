def part1(input_file):
    data = [[int(i) for i in line] for line in open(input_file).read().split('\n') if line != ""]

    len_x = len(data[0])
    len_y = len(data)

    total = 0

    for y in range(0, len_y):
        for x in range(0, len_x):
            if data[y][x] == 0:
                score = len(set(reachable(data,y,x,len_x,len_y)))
                total += score

    print(total)

def reachable(data, y, x, len_x, len_y):
    summits = []

    if data[y][x] == 9:
        return [(x, y)]

    # north
    if (y - 1) >= 0 and data[y-1][x] == (data[y][x] + 1):
        summits = summits + reachable(data, y - 1, x, len_x, len_y)
    # west
    if (x - 1) >= 0 and data[y][x-1] == (data[y][x] + 1):
        summits = summits +  reachable(data, y, x - 1, len_x, len_y)
    # south
    if (y + 1) < len_y and data[y+1][x] == (data[y][x] + 1):
        summits = summits + reachable(data, y + 1, x, len_x, len_y)
    # east
    if (x + 1) < len_x and data[y][x+1] == (data[y][x] + 1):
        summits = summits +  reachable(data, y, x + 1, len_x, len_y)

    return summits


def part2(input_file):
    data = [[-1 if i == '.' else int(i) for i in line] for line in open(input_file).read().split('\n') if line != ""]

    len_x = len(data[0])
    len_y = len(data)
    total = 0

    for y in range(0, len_y):
        for x in range(0, len_x):
            if data[y][x] == 0:
                score = trails(data,y,x,len_x,len_y)
                total += score

    print(total)

def trails(data, y, x, len_x, len_y):
    count = 0

    if data[y][x] == 9:
        return 1

    # north
    if (y - 1) >= 0 and data[y-1][x] == (data[y][x] + 1):
        count += trails(data, y - 1, x, len_x, len_y)
    # west
    if (x - 1) >= 0 and data[y][x-1] == (data[y][x] + 1):
        count += trails(data, y, x - 1, len_x, len_y)
    # south
    if (y + 1) < len_y and data[y+1][x] == (data[y][x] + 1):
        count += trails(data, y + 1, x, len_x, len_y)
    # east
    if (x + 1) < len_x and data[y][x+1] == (data[y][x] + 1):
        count += trails(data, y, x + 1, len_x, len_y)

    return count


if __name__ == '__main__':
    part2("input.txt")
