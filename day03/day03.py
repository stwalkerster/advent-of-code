import re

def part1(inputFile):
    input = open(inputFile).read().split('\n')

    total = 0

    for y in range(0, len(input)):
        for x in range(0, len(input[y])):
            if input[y][x].isdigit() and (x == 0 or not input[y][x-1].isdigit()):
                # start of number
                number_start = x
                number_end = len(input[y])

                for x2 in range(x, len(input[y])):
                    if not input[y][x2].isdigit():
                        number_end = x2
                        break

                print('found number', input[y][number_start:number_end])

                test_area = ''

                if y > 0:
                    test_area += input[y-1][max(0, number_start-1):min(number_end+1, len(input[y-1]))]

                if number_start > 0:
                    test_area += input[y][number_start-1]

                if number_end < len(input[y]):
                    test_area += input[y][number_end]

                if (y+1) < (len(input)-1):
                    test_area += input[y+1][max(0, number_start-1):min(number_end+1, len(input[y+1]))]

                test_area = re.sub('[0-9.]', '', test_area)

                if len(test_area) > 0:
                    # found part number
                    total += int(input[y][number_start:number_end])

    print(total)

def part2(inputFile):
    input = open(inputFile).read().split('\n')

    possible_gears = [ ]

    total = 0

    for y in range(0, len(input)):
        for x in range(0, len(input[y])):
            if input[y][x] == '*':
                possible_gears.append([x, y])

    print('found', len(possible_gears), 'possible gears')

    for g in possible_gears:
        surrounding_coords = [
            [g[0] - 1, g[1] - 1], [g[0] + 0, g[1] - 1], [g[0] + 1, g[1] - 1],
            [g[0] - 1, g[1] + 0],                       [g[0] + 1, g[1] + 0],
            [g[0] - 1, g[1] + 1], [g[0] + 0, g[1] + 1], [g[0] + 1, g[1] + 1],
        ]

        digits = set()

        for s in surrounding_coords:
            if s[0] < 0 or s[0] >= len(input[0]):
                continue
            if s[1] < 0 or s[1] >= len(input):
                continue

            if input[s[1]][s[0]].isdigit():
                # print('gear', g, 'has digit', input[s[1]][s[0]], 'at', s )
                digits.add(find_full_number(input, *s))

        if len(digits) == 2:
            first = digits.pop()
            second = digits.pop()
            print(g, first[3], second[3], first[3] * second[3])

            total += first[3] * second[3]
            print("    running total", total)
        else:
            print(g, "is not a gear; has", len(digits), "digits", digits)

    print(total)

def find_full_number(input, init_x, init_y):
    line = input[init_y]

    num_start = init_x
    start_set = False
    num_end = init_x
    end_set = False

    for x in range(init_x - 1, -1, -1):
        if line[x].isdigit():
            continue

        num_start = x + 1
        start_set = True
        break

    if not start_set:
        # oops. we fell off the bottom of the loop
        num_start = 0

    for x in range(init_x, len(line)):
        if line[x].isdigit():
            continue

        num_end = x - 1
        end_set = True
        break

    if not end_set:
        num_end = len(line)

    return init_y, num_start, num_end, int(line[num_start:num_end + 1])


if __name__ == '__main__':
    part2("input.txt")
