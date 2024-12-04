import re

def part1(input_file):
    data = [line for line in open(input_file).read().split('\n') if line != ""]

    total = 0

    for l in data:
        for m in re.finditer(r'mul\(([0-9]+),([0-9]+)\)', l):
            total += int(m.group(1)) * int(m.group(2))

    print(total)

def part2(input_file):
    data = [line for line in open(input_file).read().split('\n') if line != ""]

    total = 0
    enabled = True

    for l in data:
        for m in re.finditer(r"(?:do\(\))|(?:don't\(\))|(?:mul\(([0-9]+),([0-9]+)\))", l):
            if m.group(0) == 'do()':
                enabled = True
                continue

            if m.group(0) == 'don\'t()':
                enabled = False
                continue

            if enabled:
                total += int(m.group(1)) * int(m.group(2))

    print(total)


if __name__ == '__main__':
    part2("input.txt")
