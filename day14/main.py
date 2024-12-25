import re
from PIL import Image

class Robot:
    def __init__(self, definition):
        pattern = re.compile(r'^p=(?P<px>[0-9]+),(?P<py>[0-9]+) v=(?P<vx>-?[0-9]+),(?P<vy>-?[0-9]+)$')
        match = pattern.match(definition)

        self.position = (int(match.group("px")), int(match.group("py")))
        self.vector = (int(match.group("vx")), int(match.group("vy")))

    def move(self, bounds):
        self.position = (self.position[0] + self.vector[0], self.position[1] + self.vector[1])
        self.position = (self.position[0] % bounds[0], self.position[1] % bounds[1])

    def quadrant(self, bounds):
        x_middle = bounds[0] // 2
        y_middle = bounds[1] // 2

        if self.position[0] == x_middle or self.position[1] == y_middle:
            return None

        if self.position[0] < x_middle:
            if self.position[1] < y_middle:
                return 1
            else:
                return 2
        else:
            if self.position[1] < y_middle:
                return 3
            else:
                return 4


def part1(input_file):
    field_bounds = (101, 103) if input_file == "input.txt" else (11, 7)
    data = [Robot(line) for line in open(input_file).read().split('\n') if line != ""]

    for _ in range(100):
        for r in data:
            r.move(field_bounds)


    q = [
        sum(1 for r in data if r.quadrant(field_bounds) == 1),
        sum(1 for r in data if r.quadrant(field_bounds) == 2),
        sum(1 for r in data if r.quadrant(field_bounds) == 3),
        sum(1 for r in data if r.quadrant(field_bounds) == 4),
    ]

    return q[0] * q[1] * q[2] * q[3]



def part2(input_file):
    field_bounds = (101, 103) if input_file == "input.txt" else (11, 7)
    data = [Robot(line) for line in open(input_file).read().split('\n') if line != ""]

    x_middle = field_bounds[0] // 2

    i = 0
    while True:
        img = Image.new("L", field_bounds)
        pixels = img.load()

        render = len(set([r.position for r in data])) == len(data)

        for r in data:
            pixels[r.position[0], r.position[1]] = 255
            r.move(field_bounds)

        if render:
            img.save(f'output/{i}.png')

        i+=1

    return None

if __name__ == '__main__':
    print(part2("input.txt"))
