from math import pow

class Card:
    def __init__(self, line):
        prefix, remainder = line.split(': ')
        winning, yours = remainder.split(' | ')
        _, id = prefix.split()
        self.id = int(id)
        self.all_winning_numbers = set([int(x) for x in winning.split()])
        self.own_numbers = set([int(x) for x in yours.split()])

    def get_my_winning_numbers(self):
        return self.all_winning_numbers.intersection(self.own_numbers)

def part1(inputFile):
    input = open('data/day04/' + inputFile).read().split('\n')

    card_data = [len(Card(i).get_my_winning_numbers()) for i in input if i != ""]

    print(card_data)

    scores = [pow(2, i - 1) for i in card_data if i > 0]

    print(sum(scores))

def part2(inputFile):
    input = open('data/day04/' + inputFile).read().split('\n')
    cards = [Card(i) for i in input if i != ""]
    card_count = {c.id: 1 for c in cards}

    for c in cards:
        number_winning = len(c.get_my_winning_numbers())
        copies = card_count[c.id]

        for won in range(c.id + 1, c.id + number_winning + 1):
            card_count[won] += copies

    print(sum(card_count.values()))

if __name__ == '__main__':
    part2("input.txt")
