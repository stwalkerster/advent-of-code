def part1(input_file):
    data = [line for line in open(input_file).read().split('\n\n') if line != ""]

    total = 0
    for pattern_data in data:
        pattern = [line for line in pattern_data.split('\n') if line != ""]
        print()
        print()
        pretty_array(pattern)

        print("Testing rows")
        row = test_reflection(pattern)

        if row is not None:
            total += (100 * row)
            continue

        print("Testing cols")
        col = test_reflection(list(zip(*pattern)))

        if col is not None:
            total += col

    print("Total:", total)


def test_reflection(pattern, dir='z', skip=None):
    for y in range(1, len(pattern)):
        if pattern[y] == pattern[y - 1]:
            y_low = y - 2
            y_high = y + 1

            matching = True
            while y_low >= 0 and y_high < len(pattern):

                if pattern[y_low] != pattern[y_high]:
                    matching = False
                    break

                y_low -= 1
                y_high += 1

            if matching and y != (skip or -1):
                print('   ', f"Reflection confirmed at {dir}={y}!")
                return y
    return None


def pretty_array(d):
    print('[')
    for l in d:
        print('   ', l)
    print(']')


def part2(input_file):
    data = [line for line in open(input_file).read().split('\n\n') if line != ""]

    total = 0
    for pattern_data in data:
        print('New Pattern.')
        pattern = [line for line in pattern_data.split('\n') if line != ""]

        orig_row = test_reflection(pattern)
        orig_col = test_reflection(list(zip(*pattern)))

        exit_loop = False
        for y in range(len(pattern)):
            for x in range(len(pattern[0])):
                local_pattern = pattern.copy()

                modified_line = list(local_pattern[y])
                modified_line[x] = '.' if modified_line[x] == '#' else '#'
                local_pattern[y] = ''.join(modified_line)

                row = test_reflection(local_pattern, dir='r', skip=orig_row)
                if row is not None and (orig_row is None or row != orig_row):
                    total += (100 * row)
                    exit_loop = True
                    break

                col = test_reflection(list(zip(*local_pattern)), dir='c', skip=orig_col)
                if col is not None and (orig_col is None or col != orig_col):
                    total += col
                    exit_loop = True
                    break

            if exit_loop:
                break

    print("Total:", total)


if __name__ == '__main__':
    part1("input.txt")
