import re


def hash(data):
    current = 0
    for c in data:
        current += ord(c)
        current *= 17
        current %= 256
    return current


class Lens:
    def __init__(self, label, focal_length):
        self.label = label
        self.focal_length = focal_length

    def __repr__(self):
        return f'[{self.label} {self.focal_length}]'


def part1(inputFile):
    input = [line for line in open(inputFile).read().replace('\n', '').split(',') if line != ""]

    print(sum([hash(i) for i in input]))


def print_boxes(b):
    for i in range(len(b)):
        if len(b[i]) > 0:
            print(f"Box {i}: ", end="")
            for lens in b[i]:
                print(lens, "", end="")
            print()


def part2(inputFile):
    input = [line for line in open(inputFile).read().replace('\n', '').split(',') if line != ""]

    boxes = [[] for i in range(256)]

    instruction_pattern = re.compile("^(?P<label>[a-z]+)(?P<operation>[-=])(?P<value>[0-9])?")

    for instruction in input:
        instr = instruction_pattern.match(instruction).groupdict()
        hashval = hash(instr["label"])

        if instr["operation"] == "-":
            for l in boxes[hashval]:
                if l.label == instr["label"]:
                    boxes[hashval].remove(l)
                    break
            continue

        handled = False
        for l in boxes[hashval]:
            if l.label == instr["label"]:
                l.focal_length = int(instr["value"])
                handled = True
                break

        if not handled:
            boxes[hashval].append(Lens(instr["label"], int(instr["value"])))

    total_power = 0
    for b in range(256):
        for l in range(len(boxes[b])):
            total_power += (b + 1) * (l + 1) * boxes[b][l].focal_length

    print_boxes(boxes)
    print(total_power)


if __name__ == '__main__':
    part2("input.txt")

