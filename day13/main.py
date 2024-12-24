import re

class Machine:
    def __init__(self, data):
        data = data.split('\n')

        button_pattern = re.compile(r'^Button [AB]: X\+(?P<x>[0-9]+), Y\+(?P<y>[0-9]+)$')
        match = button_pattern.match(data[0])
        self.button_a = (int(match.group('x')), int(match.group('y')))
        match = button_pattern.match(data[1])
        self.button_b = (int(match.group('x')), int(match.group('y')))

        prize_pattern = re.compile(r'^Prize: X=(?P<x>[0-9]+), Y=(?P<y>[0-9]+)$')
        match = prize_pattern.match(data[2])
        self.prize = (int(match.group('x')), int(match.group('y')))

    def __repr__(self):
        return f'A: {self.button_a}, B: {self.button_b}, Prize: {self.prize}'


def part1(input_file):
    data = parse(input_file)

    total_tokens = 0
    for mi in range(len(data)):
        m = data[mi]

        max_a = min( m.prize[0] // m.button_a[0], m.prize[1] // m.button_a[1])
        max_b = min( m.prize[0] // m.button_b[0], m.prize[1] // m.button_b[1])

        possibles = []

        for a_presses in range(0, max_a + 1):
            remaining_target = (m.prize[0] - (m.button_a[0] * a_presses), m.prize[1] - (m.button_a[1] * a_presses))
            b_presses = find_topup(remaining_target, m.button_b)

            if b_presses is not None:
                possibles.append((a_presses, b_presses))

        if len(possibles) > 0:
            total_tokens += min([(x[0] * 3) + x[1] for x in possibles])

    return total_tokens


def find_topup(target, button):
    if target[0] % button[0] != 0:
        return None
    if target[1] % button[1] != 0:
        return None

    x = target[0] // button[0]
    y = target[1] // button[1]

    return x if x == y else None


def part2(input_file):
    data = parse(input_file)

    return None


def parse(input_file):
    data = [Machine(machine_def) for machine_def in open(input_file).read().split('\n\n') if machine_def != ""]

    return data


if __name__ == '__main__':
    print(part1("example.txt"))
