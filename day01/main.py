from util.datafile import load_lines


def part1(input_file):
    data = load_lines(input_file)

    start = 50
    zero_count = 0

    for instr in data:
        direction = instr[0]
        amount = int(instr[1:])

        amount = amount * -1 if direction == "L" else amount

        start = (start + amount) % 100

        if start == 0:
            zero_count += 1

    return zero_count


def part2(input_file):
    data = load_lines(input_file)

    start = 50
    zero_count = 0

    for instr in data:
        direction = instr[0]
        amount = int(instr[1:])

        for i in range(amount):
            step = -1 if direction == "L" else 1
            start = (start + step) % 100

            if start == 0:
                zero_count += 1

    return zero_count


if __name__ == '__main__':
    print(part2("input.txt"))
