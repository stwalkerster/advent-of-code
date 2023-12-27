from termcolor import colored


def display(d):
    print()
    for line in d:
        for cell in line:
            if cell == '#':
                print(colored(cell, 'white', 'on_white'), end="")
            elif cell == 'x':
                print(colored(cell, 'blue', 'on_blue'), end="")
            else:
                print(colored(cell, 'dark_grey', 'on_dark_grey'), end="")
        print()


def part1(input_file):
    data = [line for line in open(input_file).read().split('\n') if line != ""]

    # calculate bounds
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0

    position = (0, 0)

    for line in data:
        direction, dstr, _ = line.split(' ')

        distance = int(dstr)

        if direction == 'R':
            position = (position[0] + distance, position[1])
            max_x = max(max_x, position[0])
        if direction == 'L':
            position = (position[0] - distance, position[1])
            min_x = min(min_x, position[0])
        if direction == 'U':
            position = (position[0], position[1] - distance)
            min_y = min(min_y, position[1])
        if direction == 'D':
            position = (position[0], position[1] + distance)
            max_y = max(max_y, position[1])

    print(min_x, max_x, min_y, max_y)
    min_y -= 1
    min_x -= 1
    max_x += 1
    max_y += 1

    position = (0, 0)
    if min_y < 0:
        max_y += abs(min_y)
        position = (position[0], position[1] + abs(min_y))

    if min_x < 0:
        max_x += abs(min_x)
        position = (position[0] + abs(min_x), position[1])

    # calculate trench
    grid = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    grid[position[1]][position[0]] = '#'

    for line in data:
        direction, dstr, _ = line.split(' ')

        distance = int(dstr)
        if direction == 'R':
            for i in range(distance):
                grid[position[1]][position[0] + i] = '#'
            position = (position[0] + distance, position[1])

        if direction == 'L':
            for i in range(distance):
                grid[position[1]][position[0] - i] = '#'
            position = (position[0] - distance, position[1])

        if direction == 'U':
            for i in range(distance):
                grid[position[1] - i][position[0]] = '#'
            position = (position[0], position[1] - distance)

        if direction == 'D':
            for i in range(distance):
                grid[position[1] + i][position[0]] = '#'
            position = (position[0], position[1] + distance)

    dug_blocks = sum([sum([1 for x in range(len(grid[y])) if grid[y][x] in ('#')]) for y in range(len(grid))])
    print("trench blocks", dug_blocks)


    # flood-fill
    grid[0][0] = 'x'

    # fill edges
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if x == 0 or y == 0 or x == len(grid[y]) - 1 or y == len(grid) - 1:
                grid[y][x] = 'x'
                continue

    changed = True
    while changed:
        changed = False

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] in ('x', '#'):
                    continue

                if x - 1 >= 0 and grid[y][x - 1] == 'x':
                    grid[y][x] = 'x'
                    changed = True
                    continue

                if y - 1 >= 0 and grid[y - 1][x] == 'x':
                    grid[y][x] = 'x'
                    changed = True
                    continue

        for y in range(len(grid) - 1, 0, -1):
            for x in range(len(grid[y]) - 1, 0, -1):
                if grid[y][x] in ('x', '#'):
                    continue

                if x + 1 < len(grid[y]) and grid[y][x + 1] == 'x':
                    grid[y][x] = 'x'
                    changed = True
                    continue

                if y + 1 < len(grid) and grid[y + 1][x] == 'x':
                    grid[y][x] = 'x'
                    changed = True
                    continue

    dug_blocks = sum([sum([1 for x in range(len(grid[y])) if grid[y][x] in ('#', '.')]) for y in range(len(grid))])
    print("total blocks", dug_blocks)


def part2(input_file, mode=2):
    data = [line for line in open(input_file).read().split('\n') if line != ""]

    coord_list = []
    position = (0, 0)

    perimeter = 0

    for line in data:
        if mode == 1:
            direction, dstr, _ = line.split(' ')
            distance = int(dstr)
        else:
            _, _, hexstr = line.split(' ')
            hexstr = hexstr.replace('(', '').replace(')', '').replace('#', '')

            if hexstr[-1] == '0':
                direction = 'R'
            elif hexstr[-1] == '1':
                direction = 'D'
            elif hexstr[-1] == '2':
                direction = 'L'
            elif hexstr[-1] == '3':
                direction = 'U'

            hexstr = hexstr[:-1:]
            distance = int(hexstr, 16)

        #print(direction, distance)
        perimeter += distance


        if direction == 'R':
            position = (position[0] + distance, position[1])
            coord_list.append(position)
        if direction == 'L':
            position = (position[0] - distance, position[1])
            coord_list.append(position)
        if direction == 'U':
            position = (position[0], position[1] - distance)
            coord_list.append(position)
        if direction == 'D':
            position = (position[0], position[1] + distance)
            coord_list.append(position)

    min_x, min_y = (0, 0)
    for coord in coord_list:
        min_x = min(min_x, coord[0])
        min_y = min(min_y, coord[1])

    print("Offsets:", (min_x, min_y))

    x, y = list(zip(*coord_list))

    # shoelace
    area = (sum(i*j for i, j in zip(x, y[1:] + y[:1])) - sum(i*j for i, j in zip(x[1:] + x[:1], y)))/2
    # pick's theorem
    print(int(area + (perimeter/2) + 1))


if __name__ == '__main__':
    part2("input.txt", 2)
