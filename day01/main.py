def part1(input_file):
    data = [line.split('   ') for line in open(input_file).read().split('\n') if line != ""]

    list1 = [int(x[0]) for x in data]
    list1.sort()
    list2 = [int(x[1]) for x in data]
    list2.sort()

    deltas = [abs(x - y) for x, y in zip(list1, list2)]

    return sum(deltas)


def part2(input_file):
    data = [line.split('   ') for line in open(input_file).read().split('\n') if line != ""]

    list1 = [int(x[0]) for x in data]
    list2 = [int(x[1]) for x in data]
    list2.sort()

    similarity = 0

    for i in list1:
        similarity += i * list2.count(i)

    return similarity


if __name__ == '__main__':
    print(part2("input.txt"))
