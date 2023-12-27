def part1(inputFile):
    input = [[c for c in line] for line in open(inputFile).read().split('\n') if line != ""]

    changed = True
    while changed:
        changed = False
        for y in range(1, len(input)):
            for x in range(len(input[y])):
                if input[y][x] == "O" and input[y-1][x] == ".":
                    input[y - 1][x] = "O"
                    input[y][x] = "."
                    changed = True

    total = 0
    for i in range(len(input)):
        total += sum([1 for c in input[i] if c == 'O']) * (len(input) - i)

    print(total)


def part2(inputFile):
    input = [[c for c in line] for line in open(inputFile).read().split('\n') if line != ""]


if __name__ == '__main__':
    part1("input.txt")

