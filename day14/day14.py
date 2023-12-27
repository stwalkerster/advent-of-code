import hashlib

def part1(inputFile):
    input = [[c for c in line] for line in open(inputFile).read().split('\n') if line != ""]

    changed = True
    while changed:
        changed = False
        for y in range(1, len(input)):
            for x in range(len(input[y])):
                if input[y][x] == "O" and input[y-1][x] == ".":
                    input[y - 1][x] = "O"
                    input[y][x] = "."
                    changed = True

    total = 0
    for i in range(len(input)):
        total += sum([1 for c in input[i] if c == 'O']) * (len(input) - i)

    print(total)


def part2(inputFile):
    input = [[c for c in line] for line in open(inputFile).read().split('\n') if line != ""]

    def print_data():
        print("\n".join(["".join(l) for l in input]))
        print(hashlib.sha1("\n".join(["".join(l) for l in input]).encode('ascii')).hexdigest())

    def calculate_load():
        total = 0
        for i in range(len(input)):
            total += sum([1 for c in input[i] if c == 'O']) * (len(input) - i)
        return total

    def roll_north():
        changed = True
        while changed:
            changed = False
            for y in range(1, len(input)):
                for x in range(len(input[y])):
                    if input[y][x] == "O" and input[y-1][x] == ".":
                        input[y - 1][x] = "O"
                        input[y][x] = "."
                        changed = True

    def roll_south():
        changed = True
        while changed:
            changed = False
            for y in range(len(input)-2, -1, -1):
                for x in range(len(input[y])):
                    if input[y][x] == "O" and input[y+1][x] == ".":
                        input[y + 1][x] = "O"
                        input[y][x] = "."
                        changed = True

    def roll_west():
        changed = True
        while changed:
            changed = False
            for x in range(1, len(input[0])):
                for y in range(len(input)):
                    if input[y][x] == "O" and input[y][x-1] == ".":
                        input[y][x - 1] = "O"
                        input[y][x] = "."
                        changed = True

    def roll_east():
        changed = True
        while changed:
            changed = False
            for x in range(len(input[0])-2, -1, -1):
                for y in range(len(input)):
                    if input[y][x] == "O" and input[y][x+1] == ".":
                        input[y][x + 1] = "O"
                        input[y][x] = "."
                        changed = True

    def cycle():
        roll_north()
        roll_west()
        roll_south()
        roll_east()

    iterations = 1000000000

    cache = dict()

    restart_point = 0
    for i in range(iterations):
        cycle()

        sha = hashlib.sha1("\n".join(["".join(l) for l in input]).encode('ascii')).hexdigest()

        load = calculate_load()
        print("  Cycle %d = %s, load %d" % (i, sha, load))

        if sha not in cache:
            cache[sha] = (i, load)
        else:
            if restart_point == 0:
                cycle_length = i - cache[sha][0]
                cycle_offset = cache[sha][0]
                total_cycles = int((iterations - cycle_offset) / cycle_length)

                restart_point = cycle_offset + (cycle_length * (total_cycles-2)) + 1
                print("LOOPING! current: %d, c_offset: %d, c_length: %d, total_cyc: %d, restart: %d" % (i, cycle_offset, cycle_length, total_cycles, restart_point))
                break

    if restart_point != 0:
        print("Restarting at", restart_point, "until", iterations)

        sha = hashlib.sha1("\n".join(["".join(l) for l in input]).encode('ascii')).hexdigest()
        load = calculate_load()
        print("  Startpoint %s, load %d" % ( sha, load))

        for i in range(restart_point, iterations):
            cycle()
            sha = hashlib.sha1("\n".join(["".join(l) for l in input]).encode('ascii')).hexdigest()
            load = calculate_load()
            print("  Cycle %d = %s, load %d" % (i, sha, load))

    #print_data()

    print()
    total = calculate_load()

    print("load:", total)




if __name__ == '__main__':
    part2("input.txt")

