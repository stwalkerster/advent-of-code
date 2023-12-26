from termcolor import colored
from math import ceil

# up    = -y
# down  = +y
# left  = -x
# right = +x

class Cell:
    def __init__(self, x, y, char):
        self.in_main_loop = None
        self.x = x
        self.y = y
        self.char = char

        if char == 'S':
            self.in_main_loop = True

        # up, right, down, left
        self.neighbors = []

    def connects_up(self):
        # if self.neighbors[0] is None:
        #     return False
        if self.char not in ['|', 'J', 'L', 'S']:
            return False
        return True

    def connects_down(self):
        # if self.neighbors[2] is None:
        #     return False
        if self.char not in ['|', '7', 'F', 'S']:
            return False
        return True

    def connects_left(self):
        # if self.neighbors[3] is None:
        #     return False
        if self.char not in ['-', 'J', '7', 'S']:
            return False
        return True

    def connects_right(self):
        # if self.neighbors[1] is None:
        #     return False
        if self.char not in ['-', 'L', 'F', 'S']:
            return False
        return True

    def connect(self):
        if self.in_main_loop is not None:
            return False

        if self.connects_up() and self.neighbors[0] is None:
            self.in_main_loop = False
            return True

        if self.connects_right() and self.neighbors[1] is None:
            self.in_main_loop = False
            return True

        if self.connects_down() and self.neighbors[2] is None:
            self.in_main_loop = False
            return True

        if self.connects_left() and self.neighbors[3] is None:
            self.in_main_loop = False
            return True

        if self.neighbors[0] is not None:
            if self.connects_up():
                if self.neighbors[0].connects_down():
                    if self.neighbors[0].in_main_loop is not None:
                        self.in_main_loop = self.neighbors[0].in_main_loop
                        return True
                else:
                    self.in_main_loop = False
                    return True

        if self.neighbors[1] is not None:
            if self.connects_right():
                if self.neighbors[1].connects_left():
                    if self.neighbors[1].in_main_loop is not None:
                        self.in_main_loop = self.neighbors[1].in_main_loop
                        return True
                else:
                    self.in_main_loop = False
                    return True

        if self.neighbors[2] is not None:
            if self.connects_down():
                if self.neighbors[2].connects_up():
                    if self.neighbors[2].in_main_loop is not None:
                        self.in_main_loop = self.neighbors[2].in_main_loop
                        return True
                else:
                    self.in_main_loop = False
                    return True

        if self.neighbors[3] is not None:
            if self.connects_left():
                if self.neighbors[3].connects_right():
                    if self.neighbors[3].in_main_loop is not None:
                        self.in_main_loop = self.neighbors[3].in_main_loop
                        return True
                else:
                    self.in_main_loop = False
                    return True

        return False

    def __str__(self):
        c = 'red'

        if self.in_main_loop is None:
            c = 'yellow'
        else:
            if self.in_main_loop:
                c = 'white'
            else:
                c = 'dark_grey'

        if self.char == '-':
            return colored('━', c)
        if self.char == '|':
            return colored('┃', c)
        if self.char == '7':
            return colored('┓', c)
        if self.char == 'J':
            return colored('┛', c)
        if self.char == 'F':
            return colored('┏', c)
        if self.char == 'L':
            return colored('┗', c)

        if self.char == '.':
            return colored(' ', c)
        if self.char == 'S':
            return colored('▉', c)

        return colored(self.char, c)

    def __repr__(self):
        return "%s [x%d, y%d] %s" % (self.char, self.x, self.y, self.in_main_loop)


def part1(inputFile):
    input = [line for line in open(inputFile).read().split('\n') if line != ""]
    map_size = len(input)

    map = [[Cell(x, y, input[y][x]) for x in range(map_size)] for y in range(map_size)]

    start_coords = (0, 0)

    for y in range(map_size):
        for x in range(map_size):
            if map[y][x].char == 'S':
                start_coords = (x, y)

            map[y][x].neighbors = []

            if y > 0:
                map[y][x].neighbors.append(map[y-1][x])
            else:
                map[y][x].neighbors.append(None)

            if x < map_size - 1:
                map[y][x].neighbors.append(map[y][x+1])
            else:
                map[y][x].neighbors.append(None)

            if y < map_size - 1:
                map[y][x].neighbors.append(map[y+1][x])
            else:
                map[y][x].neighbors.append(None)

            if x > 0:
                map[y][x].neighbors.append(map[y][x-1])
            else:
                map[y][x].neighbors.append(None)

    result = True
    iter_count = 0
    while result:
        result = False
        for y in range(map_size):
            for x in range(map_size):

                result = map[y][x].connect() or result

        iter_count += 1
        # print_map(map)
        # print(result)

    in_loop = sum([sum([1 for x in range(map_size) if map[y][x].in_main_loop]) for y in range(map_size)])
    print_map(map)
    print()
    print("In loop:", in_loop, "; Max path:", ceil((in_loop - 1)/2))


def print_map(map):
    for row in map:
        for cell in row:
            print(str(cell), end="")
        print()


def part2(inputFile):
    input = open(inputFile).read().split('\n')


if __name__ == '__main__':
    part1("input.txt")

