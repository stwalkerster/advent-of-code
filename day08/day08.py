import re
import math

def parse(inputFile):
    d, g = open(inputFile).read().split('\n\n')
    d = d.split(' ')[0]

    g = g.split('\n')

    graph = dict()
    for i in g:
        if i == "": continue
        m = re.match('^(...) = \\((...), (...)\\)$', i)
        graph[m.group(1)] = (m.group(2), m.group(3))

    return d, graph

def part1(inputFile):
    directions, graph = parse(inputFile)

    direction_position = 0
    steps = 0
    current = "AAA"
    while current != "ZZZ":

        if directions[direction_position] == "L":
            current = graph[current][0]
        else:
            current = graph[current][1]

        steps += 1
        direction_position = (direction_position + 1) % len(directions)

    print(steps)


def part2(inputFile):
    directions, graph = parse(inputFile)

    nodes = [i for i in graph.keys() if i.endswith('A')]

    step_count = []
    for n in nodes:
        steps = 0
        current = n
        direction_position = 0

        while True:
            if directions[direction_position] == "L":
                current = graph[current][0]
            else:
                current = graph[current][1]

            direction_position = (direction_position + 1) % len(directions)
            steps += 1

            if current.endswith('Z'):
                print(n, steps, current)
                step_count.append(steps)
                break

    print(step_count)

    print(math.lcm(*step_count))


if __name__ == '__main__':
    part2("input.txt")

