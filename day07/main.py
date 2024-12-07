def part1(input_file):
    data = [line for line in open(input_file).read().split('\n') if line != ""]

    def test(target: int, numbers: list) -> bool:
        if len(numbers) == 1:
            return target == numbers[0]

        if test(target, [numbers[0] * numbers[1]] + numbers[2:]):
            return True

        if test(target, [numbers[0] + numbers[1]] + numbers[2:]):
            return True

        return False

    total = 0

    for line in data:
        raw_target, raw_numbers = line.split(': ')
        target = int(raw_target)
        numbers = [int(x) for x in raw_numbers.split(' ')]

        if test(target, numbers):
            total += target

    print(total)


def part2(input_file):
    data = [line for line in open(input_file).read().split('\n') if line != ""]

    def test(target: int, numbers: list) -> bool:
        if len(numbers) == 1:
            return target == numbers[0]

        if test(target, [numbers[0] * numbers[1]] + numbers[2:]):
            return True

        if test(target, [numbers[0] + numbers[1]] + numbers[2:]):
            return True

        if test(target, [int(str(numbers[0]) + str(numbers[1]))] + numbers[2:]):
            return True

        return False

    total = 0

    for line in data:
        raw_target, raw_numbers = line.split(': ')
        target = int(raw_target)
        numbers = [int(x) for x in raw_numbers.split(' ')]

        if test(target, numbers):
            total += target

    print(total)

if __name__ == '__main__':
    part2("input.txt")
