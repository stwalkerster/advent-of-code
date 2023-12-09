def part1(inputFile):
    sequences = []
    for line in open(inputFile).read().split('\n'):
        if line == "": continue
        sequences.append([int(i) for i in line.split()])

    total = 0
    for s in sequences:
        next = find_next(s)
        total += next
        #print(s, next)

    print(total)

def find_next(s):
    aggregated_list = [i[1] - i[0] for i in zip(s[:-1:], s[1::])]

    if len(aggregated_list) > 0 and len([i for i in aggregated_list if i != 0]) == 0:
        return s[-1]

    return find_next(aggregated_list) + s[-1]


def part2(inputFile):
    sequences = []
    for line in open(inputFile).read().split('\n'):
        if line == "": continue
        sequences.append([int(i) for i in line.split()])

    total = 0
    for s in sequences:
        next = find_next(s[::-1])
        total += next
        #print(s[::-1], next)

    print(total)




if __name__ == '__main__':
    part1("input.txt")
    part2("input.txt")

