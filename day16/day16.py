from termcolor import colored


def analyze_beam(direction, next_cell, grid, energised, splitters_triggered):
    while True:
        x, y = next_cell
        if x < 0 or x >= len(grid[0]):
            return
        if y < 0 or y >= len(grid):
            return

        char = grid[y][x]

        energised[y][x] = 1

        if char == '.':
            next_cell = tuple(map(sum, zip(direction, next_cell)))
            continue
        if char == '-':
            if direction[1] == 0:
                next_cell = tuple(map(sum, zip(direction, next_cell)))
                continue
            else:
                if next_cell in splitters_triggered:
                    return

                splitters_triggered.append(next_cell)

                dir_1 = (-1, 0)
                next_1 = tuple(map(sum, zip(dir_1, next_cell)))
                dir_2 = (1, 0)
                next_2 = tuple(map(sum, zip(dir_2, next_cell)))
                analyze_beam(dir_1, next_1, grid, energised, splitters_triggered)
                analyze_beam(dir_2, next_2, grid, energised, splitters_triggered)
                return

        if char == '|':
            if direction[0] == 0:
                next_cell = tuple(map(sum, zip(direction, next_cell)))
                continue
            else:
                if next_cell in splitters_triggered:
                    return

                splitters_triggered.append(next_cell)

                dir_1 = (0, -1)
                next_1 = tuple(map(sum, zip(dir_1, next_cell)))
                dir_2 = (0, 1)
                next_2 = tuple(map(sum, zip(dir_2, next_cell)))
                analyze_beam(dir_1, next_1, grid, energised, splitters_triggered)
                analyze_beam(dir_2, next_2, grid, energised, splitters_triggered)
                return

        if char == '\\':
            direction = (direction[1], direction[0])
            next_cell = tuple(map(sum, zip(direction, next_cell)))
            continue

        if char == '/':
            direction = (direction[1] * -1, direction[0] * -1)
            next_cell = tuple(map(sum, zip(direction, next_cell)))
            continue

def part1(input_file):
    grid = [line for line in open(input_file).read().split('\n') if line != ""]

    initial_direction = (1, 0)
    initial_cell = (0, 0)

    energised, total_energised = run_analysis(grid, initial_cell, initial_direction)

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if energised[y][x] == 1:
                print(colored(grid[y][x], "black", "on_light_yellow"), end="")
            else:
                print(colored(grid[y][x], "light_grey"), end="")
        print()

    print(total_energised)


def run_analysis(grid, initial_cell, initial_direction):
    energised = [[0 for x in range(len(grid[y]))] for y in range(len(grid))]
    splitters_triggered = []
    analyze_beam(initial_direction, initial_cell, grid, energised, splitters_triggered)
    total_energised = sum([sum([energised[y][x] for x in range(len(grid[y]))]) for y in range(len(grid))])
    return energised, total_energised


def part2(input_file):
    grid = [line for line in open(input_file).read().split('\n') if line != ""]

    max_energised = 0

    # left edge
    for y in range(len(grid)):
        initial_direction = (1, 0)
        initial_cell = (0, y)

        _, total_energised = run_analysis(grid, initial_cell, initial_direction)
        max_energised = max(max_energised, total_energised)

    # right edge
    for y in range(len(grid)):
        initial_direction = (-1, 0)
        initial_cell = (len(grid[0]) - 1, y)

        _, total_energised = run_analysis(grid, initial_cell, initial_direction)
        max_energised = max(max_energised, total_energised)

    # top edge
    for x in range(len(grid[0])):
        initial_direction = (0, 1)
        initial_cell = (x, 0)

        _, total_energised = run_analysis(grid, initial_cell, initial_direction)
        max_energised = max(max_energised, total_energised)

    # bottom edge
    for x in range(len(grid[0])):
        initial_direction = (0, -1)
        initial_cell = (x, len(grid) - 1)

        _, total_energised = run_analysis(grid, initial_cell, initial_direction)
        max_energised = max(max_energised, total_energised)


    print(max_energised)


if __name__ == '__main__':
    part2("input.txt")

