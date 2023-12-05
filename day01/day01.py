import re


def part1(inputFile):
    input = open(inputFile).read().split('\n')

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
    input = open(inputFile).read().split('\n')

    total = 0
    for l in input:
        if l == "":
            continue

        pattern = r'one|two|three|four|five|six|seven|eight|nine'
        matches = re.search(pattern + r'|\d', l)

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

        if matches.group(0).isdigit():
            first = matches.group(0)
        else:
            first = lookup[matches.group(0)]


        matches = re.search(pattern[::-1] + r'|\d', l[::-1])

        if matches.group(0).isdigit():
            last = matches.group(0)
        else:
            last = lookup[matches.group(0)[::-1]]

        #print(l, '|',  first, '/', last, '=', int(first+last))

        total += int(first + last)
    print(total)

if __name__ == '__main__':
    part2("input.txt")

