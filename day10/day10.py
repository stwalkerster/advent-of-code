from termcolor import colored
from math import ceil

# up    = -y
# down  = +y
# left  = -x
# right = +x

class Cell:
    def __init__(self, x, y, char):
        self.in_main_loop = None
        self.external = False
        self.x = x
        self.y = y
        self.char = char

        if char == 'S':
            self.in_main_loop = True
        if char == '.':
            self.in_main_loop = False

        # up, right, down, left
        self.neighbors = []

    def connects_up(self):
        if self.char not in ['|', 'J', 'L', 'S']:
            return False
        return True

    def connects_down(self):
        if self.char not in ['|', '7', 'F', 'S']:
            return False
        return True

    def connects_left(self):
        if self.char not in ['-', 'J', '7', 'S']:
            return False
        return True

    def connects_right(self):
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

    def calculated_char(self):
        if self.char != 'S':
            return self.char

        if self.neighbors[0] is not None and self.neighbors[0].in_main_loop and self.neighbors[0].connects_down():
            # Must be |, J, L
            if self.neighbors[2].in_main_loop and self.neighbors[2].connects_up():
                return '|'
            if self.neighbors[1].in_main_loop and self.neighbors[1].connects_left():
                return 'L'
            return 'J'
        else:
            # Must be -, F, 7
            if self.neighbors[2].in_main_loop and not self.neighbors[2].connects_up():
                return '-'
            if self.neighbors[1].in_main_loop and not self.neighbors[1].connects_left():
                return '7'
            return 'F'

    def __str__(self):
        c = 'red'
        b = 'on_black'

        if self.in_main_loop is None:
            c = 'yellow'
        else:
            if self.in_main_loop:
                c = 'white'
            else:
                if not self.external:
                    b = 'on_green'
                    c = 'green'
                else:
                    c = 'dark_grey'

        def box(char):
            if char == '-':
                return '━'
            if char == '|':
                return '┃'
            if char == '7':
                return '┓'
            if char == 'J':
                return '┛'
            if char == 'F':
                return '┏'
            if char == 'L':
                return '┗'
            if char == '.':
                return '.'
            return char

        if self.char == 'S':
            return colored(box(self.calculated_char()), 'light_grey', 'on_white')

        return colored(box(self.char), c, b)

    def __repr__(self):
        return "%s [x%d, y%d] M:%s E:%s" % (self.char, self.x, self.y, self.in_main_loop, self.external)


def part1(inputFile):
    input = [line for line in open(inputFile).read().split('\n') if line != ""]
    map_size = len(input)

    map = [[Cell(x, y, input[y][x]) for x in range(map_size)] for y in range(map_size)]

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
    input = [line for line in open(inputFile).read().split('\n') if line != ""]
    y_map_size = len(input)
    x_map_size = len(input[0])

    map = [[Cell(x, y, input[y][x]) for x in range(x_map_size)] for y in range(y_map_size)]

    for y in range(y_map_size):
        for x in range(x_map_size):
            if map[y][x].char == 'S':
                start_coords = (x, y)

            map[y][x].neighbors = []

            if y > 0:
                map[y][x].neighbors.append(map[y-1][x])
            else:
                map[y][x].neighbors.append(None)

            if x < x_map_size - 1:
                map[y][x].neighbors.append(map[y][x+1])
            else:
                map[y][x].neighbors.append(None)

            if y < y_map_size - 1:
                map[y][x].neighbors.append(map[y+1][x])
            else:
                map[y][x].neighbors.append(None)

            if x > 0:
                map[y][x].neighbors.append(map[y][x-1])
            else:
                map[y][x].neighbors.append(None)

    result = True
    while result:
        result = False
        for y in range(y_map_size):
            for x in range(x_map_size):
                result = map[y][x].connect() or result

    #print_map(map)
    for y in range(y_map_size):
        inside = False
        border = None
        for x in range(x_map_size):
            if map[y][x].in_main_loop:
                char = map[y][x].calculated_char()
                if char == '-':
                    pass
                if char == '|':
                    inside = not inside
                if char in ('F', 'L', '7', 'J'):
                    if border is None:
                        border = char
                    else:
                        if (border == 'F' and char == '7') or (border == 'L' and char == 'J'):
                            border = None
                        else:
                            border = None
                            inside = not inside
            else:
                map[y][x].external = not inside
                map[y][x].in_main_loop = False

    internal = sum([sum([1 for x in range(x_map_size) if not map[y][x].external and not map[y][x].in_main_loop]) for y in range(y_map_size)])
    print_map(map)
    print()
    print("Internal:", internal)


if __name__ == '__main__':
    part2("input.txt")

