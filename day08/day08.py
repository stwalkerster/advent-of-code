import re

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

    direction_position = 0
    steps = 0

    nodes = [i for i in graph.keys() if i.endswith('A')]

    print("Analysing %d nodes" % len(nodes), nodes)

    while len(nodes) != len([1 for i in nodes if i.endswith('Z')]):
        for i in range(0, len(nodes)):
            if directions[direction_position] == "L":
                nodes[i] = graph[nodes[i]][0]
            else:
                nodes[i] = graph[nodes[i]][1]

        steps += 1
        direction_position = (direction_position + 1) % len(directions)

    print(steps)


if __name__ == '__main__':
    part2("input.txt")

