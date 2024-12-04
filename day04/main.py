def part1(input_file):
    data = [[c for c in line] for line in open(input_file).read().split('\n') if line != ""]

    def check_direction(d_x, d_y):
        buffer_x_start = 0 if d_x >= 0 else len(target) - 1
        buffer_x_end = 0 if d_x <= 0 else len(target) - 1
        buffer_y_start = 0 if d_y >= 0 else len(target) - 1
        buffer_y_end = 0 if d_y <= 0 else len(target) - 1

        found = 0

        for y in range(buffer_y_start, len(data) - buffer_y_end):
            for x in range(buffer_x_start, len(data[0]) - buffer_x_end):
                result = check_target(x, y, d_x, d_y, target)
                if result:
                    found += 1

        return found

    def check_target(x, y, d_x, d_y, target):
        if data[y][x] == target[0]:
            if len(target) == 1:
                return True
            else:
                return check_target(x + d_x, y + d_y, d_x, d_y, target[1:])

        return False

    if not all([len(x) == len(data[0]) for x in data]):
        print("dataset is jagged?")
        exit(1)

    target = ['X', 'M', 'A', 'S']

    d_e = check_direction(1, 0)
    d_w = check_direction(-1, 0)
    d_n = check_direction(0, -1)
    d_s = check_direction(0, 1)
    d_nw = check_direction(-1, -1)
    d_ne = check_direction(1, -1)
    d_se = check_direction(1, 1)
    d_sw = check_direction(-1, 1)

    print(sum([d_e, d_w, d_n, d_s, d_se, d_sw, d_ne, d_nw]))


def part2(input_file):
    data = [[c for c in line] for line in open(input_file).read().split('\n') if line != ""]

    def check_mas(x, y):
        result = True

        # check nw-se
        if data[y-1][x-1] == 'M' and data[y+1][x+1] == 'S' \
        or data[y-1][x-1] == 'S' and data[y+1][x+1] == 'M':
            pass
        else:
            result = False

        # check ne-sw
        if data[y+1][x-1] == 'M' and data[y-1][x+1] == 'S' \
        or data[y+1][x-1] == 'S' and data[y-1][x+1] == 'M':
            pass
        else:
            result = False

        return result

    found = 0

    for y in range(1, len(data) - 1):
        for x in range(1, len(data[0]) - 1):
            if data[y][x] == 'A' and check_mas(x, y):
                found += 1

    print(found)


if __name__ == '__main__':
    part2("input.txt")
