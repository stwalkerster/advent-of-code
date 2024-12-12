def part1(input_file):
    data = [list(line) for line in open(input_file).read().split('\n') if line != ""]

    len_y = len(data)
    len_x = len(data[0])

    frequencies = dict()

    for y in range(0, len_y):
        for x in range(0, len_x):
            if data[y][x] != '.':
                if data[y][x] not in frequencies:
                    frequencies[data[y][x]] = []
                frequencies[data[y][x]].append((x, y))

    antinodes = set()

    # pairwise?
    for f in frequencies:
        for i in range(0, len(frequencies[f]) - 1):
            for j in range(i + 1, len(frequencies[f])):
                dx = frequencies[f][i][0] - frequencies[f][j][0]
                dy = frequencies[f][i][1] - frequencies[f][j][1]

                lower = (frequencies[f][i][0] + dx, frequencies[f][i][1] + dy)
                upper = (frequencies[f][j][0] - dx, frequencies[f][j][1] - dy)

                if 0 <= lower[0] < len_x and 0 <= lower[1] < len_y:
                    antinodes.add(lower)

                if 0 <= upper[0] < len_x and 0 <= upper[1] < len_y:
                    antinodes.add(upper)

    print(len(antinodes))


def part2(input_file):
    data = [list(line) for line in open(input_file).read().split('\n') if line != ""]

    len_y = len(data)
    len_x = len(data[0])

    frequencies = dict()

    for y in range(0, len_y):
        for x in range(0, len_x):
            if data[y][x] != '.':
                if data[y][x] not in frequencies:
                    frequencies[data[y][x]] = []
                frequencies[data[y][x]].append((x, y))

    antinodes = set()

    def in_range(node):
        if 0 <= node[0] < len_x and 0 <= node[1] < len_y:
            return True
        return False

    # pairwise?
    for f in frequencies:
        for i in range(0, len(frequencies[f]) - 1):
            for j in range(i + 1, len(frequencies[f])):
                dx = frequencies[f][i][0] - frequencies[f][j][0]
                dy = frequencies[f][i][1] - frequencies[f][j][1]

                antinodes.add(frequencies[f][i])
                antinodes.add(frequencies[f][j])

                candidate = frequencies[f][i]

                while True:
                    candidate = (candidate[0] + dx, candidate[1] + dy)

                    if in_range(candidate):
                        antinodes.add(candidate)
                    else:
                        break

                candidate = frequencies[f][j]

                while True:
                    candidate = (candidate[0] - dx, candidate[1] - dy)

                    if in_range(candidate):
                        antinodes.add(candidate)
                    else:
                        break

    print(len(antinodes))

if __name__ == '__main__':
    part2("input.txt")
