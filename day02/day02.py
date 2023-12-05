import re

def parse(inputFile):
    input = open(inputFile).read().split('\n')

    games = []
    for line in input:
        if line == "":
            continue

        (prefix, raw_rounds) = line.split(': ')
        game_id = prefix.split(' ')[1]

        rounds = raw_rounds.split('; ')
        parsed_rounds = []
        for g in rounds:
            cubes = g.split(', ')
            cube_set = {'red': 0, 'green': 0, 'blue': 0}
            for c in cubes:
                (k,v) = c.split(' ')
                cube_set[v] = int(k)
            parsed_rounds.append(cube_set)

        game = {'id': int(game_id),  'rounds': parsed_rounds}
        games.append(game)

    return games

def part1(inputFile):
    games = parse(inputFile)

    total = 0
    for g in games:
        possible = True
        for r in g['rounds']:
            if r['red'] > 12:
                possible = False
                break
            if r['green'] > 13:
                possible = False
                break

            if r['blue'] > 14:
                possible = False
                break


        if possible:
            total += g['id']

    print(total)

def part2(inputFile):
    games = parse(inputFile)
    total = 0

    for g in games:
        maxR = 0
        maxG = 0
        maxB = 0

        for r in g['rounds']:
            maxR = max(maxR, r['red'])
            maxG = max(maxG, r['green'])
            maxB = max(maxB, r['blue'])

        total += maxR*maxG*maxB

    print(total)

if __name__ == '__main__':
    part2("input.txt")
