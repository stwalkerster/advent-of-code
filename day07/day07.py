from math import pow

class Hand:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = int(bid)

    def __repr__(self):
        return self.hand + " " + str(self.bid)

    def aggregate_hand(self):
        self.aggregate = []

        h = self.hand

        while len(h) > 0:
            l = len(h)
            c = h[0]
            h = h.replace(c, '')
            n = l - len(h)
            self.aggregate.append(n)

    def type(self):
        self.aggregate_hand()

        # five of a kind
        if self.aggregate[0] == 5:
            return 5

        # four of a kind
        if 4 in self.aggregate:
            return 4

        # full house (3k + 2k)
        if 3 in self.aggregate and 2 in self.aggregate:
            return 3.5

        # three of a kind
        if 3 in self.aggregate:
            return 3

        # two pair
        if self.aggregate == [2,2,1] or self.aggregate == [2,1,2] or self.aggregate == [1,2,2]:
            return 2

        # one pair
        if 2 in self.aggregate:
            return 1

        return 0

    def strength(self):
        map = {
            'A': 14,
            'K': 13,
            'Q': 12,
            'J': 11,
            'T': 10
        }

        total = 0

        for x in range(0, len(self.hand)):
            val = 0
            if self.hand[x].isnumeric():
                val = int(self.hand[x])
            else:
                val = map[self.hand[x]]

            total += (val * pow(10, 2*(4 - x)))

        total += self.type() * pow(10,10)#

        return total


def part1(inputFile):
    input_data = open(inputFile).read().split('\n')
    hands = [Hand(*i1.split()) for i1 in input_data if i1 != ""]

    sorted_hands = sorted(hands, key=lambda h: h.strength())

    total = 0
    for i in range(0, len(sorted_hands)):
        total += sorted_hands[i].bid * (i+1)

    print(total)


class Hand2:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = int(bid)

    def __repr__(self):
        return self.hand + " " + str(self.bid)

    def type(self):
        self.aggregate = []

        jokers = 0
        h = self.hand
        if 'J' in h:
            l = len(h)
            h = h.replace('J', '')
            jokers = l - len(h)

        while len(h) > 0:
            l = len(h)
            c = h[0]
            h = h.replace(c, '')
            n = l - len(h)
            self.aggregate.append(n)

        self.aggregate.sort(reverse=True)

        if jokers == 5:
            return 5

        # five of a kind
        if (self.aggregate[0] + jokers) == 5:
            return 5

        # four of a kind
        if (self.aggregate[0] + jokers) == 4:
            return 4

        # full house (3k + 2k)
        if (self.aggregate[0] + jokers) == 3 and self.aggregate[1] == 2:
            return 3.5

        # three of a kind
        if (self.aggregate[0] + jokers) == 3:
            return 3

        # two pair
        if self.aggregate == [2, 2, 1]:
            return 2

        # one pair
        if self.aggregate[0] == 2 or (self.aggregate[0] == 1 and jokers == 1):
            return 1

        return 0

    def strength(self):
        map = {
            'A': 14,
            'K': 13,
            'Q': 12,
            'J': 1,
            'T': 10
        }

        total = 0

        for x in range(0, len(self.hand)):
            val = 0
            if self.hand[x].isnumeric():
                val = int(self.hand[x])
            else:
                val = map[self.hand[x]]

            total += (val * pow(10, 2*(4 - x)))

        total += self.type() * pow(10, 10)

        return total


def part2(inputFile):
    input_data = open(inputFile).read().split('\n')
    hands = [Hand2(*i1.split()) for i1 in input_data if i1 != ""]

    sorted_hands = sorted(hands, key=lambda h: h.strength())

    total = 0
    for i in range(0, len(sorted_hands)):
        print(i + 1, sorted_hands[i], sorted_hands[i].type(), sorted_hands[i].strength())
        total += sorted_hands[i].bid * (i+1)

    print(total)


if __name__ == '__main__':
    # part2("example.txt")
    part2("input.txt")

