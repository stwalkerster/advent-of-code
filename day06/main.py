def part1(input_file):
    data = [[cell for cell in line] for line in open(input_file).read().split('\n') if line != ""]

    guard = (-1, -1)
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    direction = 0

    # find guard
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '^':
                guard = (x, y)
                data[y][x] = 'X'

    # map route
    while len(data[0]) > guard[0] >= 0 and len(data) > guard[1] >= 0:
        next = tuple(map(sum,zip(guard,directions[direction])))

        if not (len(data[0]) > next[0] >= 0 and len(data) > next[1] >= 0):
            guard = next
            continue

        if data[next[1]][next[0]] == '#':
            direction = (direction + 1) % len(directions)
            continue

        data[next[1]][next[0]] = 'X'
        guard = next

    count = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == 'X':
                count += 1

    print(count)




def part2(input_file):
    data = [[cell for cell in line] for line in open(input_file).read().split('\n') if line != ""]

    guard_origin = (-1, -1)
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    # find guard
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '^':
                guard_origin = (x, y)
                data[y][x] = '.'

    def route_loops(obstacle):
        visited = [[[] for _ in data_y] for data_y in data]
        direction = 0
        guard = (guard_origin[0], guard_origin[1])

        while len(data[0]) > guard[0] >= 0 and len(data) > guard[1] >= 0:
            next = tuple(map(sum, zip(guard, directions[direction])))

            if not (len(data[0]) > next[0] >= 0 and len(data) > next[1] >= 0):
                return False

            if data[next[1]][next[0]] == '#' \
                    or (obstacle[0] == next[0] and obstacle[1] == next[1]):
                direction = (direction + 1) % len(directions)
                continue

            if direction in visited[next[1]][next[0]]:
                return True

            visited[next[1]][next[0]].append(direction)
            guard = next

        return False

    count = 0

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '#':
                continue
            if route_loops((x,y)):
                count += 1

    print(count)

if __name__ == '__main__':
    part2("input.txt")
