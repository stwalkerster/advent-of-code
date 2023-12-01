import re


def part1(inputFile):
    input = open('data/day01/' + inputFile).read().split('\n')

    total = 0
    for l in input:
        if l == "":
            continue

        first = None
        last = None
        for c in l:
            if c.isdigit():
                first = c
                break
        for c in l[::-1]:
            if c.isdigit():
                last = c
                break

        total += int(first + last)
    print(total)

def part2(inputFile):
    input = open('data/day01/' + inputFile).read().split('\n')

    total = 0
    for l in input:
        if l == "":
            continue

        matches = re.findall(r'one|two|three|four|five|six|seven|eight|nine|\d', l)

        first = None
        last = None

        lookup = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9',
        }

        if matches[0].isdigit():
            first = matches[0]
        else:
            first = lookup[matches[0]]

        if matches[-1].isdigit():
            last = matches[-1]
        else:
            last = lookup[matches[-1]]

        print(l, '|', matches[0], first, '/', matches[-1], last, '=', int(first+last))

        total += int(first + last)
    print(total)

if __name__ == '__main__':
    part2("input.txt")

