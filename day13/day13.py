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


def test_reflection(pattern):
    for y in range(1, len(pattern)):
        if pattern[y] == pattern[y - 1]:
            print('   ', f"possible reflection at z={y}?")

            y_low = y - 2
            y_high = y + 1

            matching = True
            while y_low >= 0 and y_high < len(pattern):

                if pattern[y_low] != pattern[y_high]:
                    matching = False
                    print('   ', f"Reflection failed: {pattern[y_low]} != {pattern[y_high]}")
                    break

                y_low -= 1
                y_high += 1

            if matching:
                print('   ', f"Reflection confirmed!")
                return y
    return None


def pretty_array(d):
    print('[')
    for l in d:
        print('   ', l)
    print(']')


def part2(input_file):
    data = [line for line in open(input_file).read().split('\n\n') if line != ""]


if __name__ == '__main__':
    part1("input.txt")
