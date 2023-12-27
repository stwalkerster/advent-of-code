def part1(inputFile):
    input = [line for line in open(inputFile).read().split('\n') if line != ""]

    all_missing_x = set(range(len(input[0])))
    all_missing_y = []
    galaxies = []

    for y in range(len(input)):
        missing = []
        y_has_galaxy = False
        for x in range(len(input[y])):
            if input[y][x] == '.':
                missing.append(x)
            if input[y][x] == '#':
                galaxies.append((x, y))
                y_has_galaxy = True
        all_missing_x.intersection_update(missing)
        if not y_has_galaxy:
            all_missing_y.append(y)

    all_missing_x = list(all_missing_x)

    distances = []

    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            dx = (abs(galaxies[i][0] - galaxies[j][0])
                  + sum([1 for a in all_missing_x if galaxies[i][0] < a < galaxies[j][0]])
                  + sum([1 for a in all_missing_x if galaxies[j][0] < a < galaxies[i][0]]))
            dy = (abs(galaxies[i][1] - galaxies[j][1])
                  + sum([1 for a in all_missing_y if galaxies[i][1] < a < galaxies[j][1]])
                  + sum([1 for a in all_missing_y if galaxies[j][1] < a < galaxies[i][1]]))
            distances.append((dx+dy, i+1, j+1))

    print(sum([d[0] for d in distances]))

def part2(inputFile):
    input = [line for line in open(inputFile).read().split('\n') if line != ""]

    all_missing_x = set(range(len(input[0])))
    all_missing_y = []
    galaxies = []

    for y in range(len(input)):
        missing = []
        y_has_galaxy = False
        for x in range(len(input[y])):
            if input[y][x] == '.':
                missing.append(x)
            if input[y][x] == '#':
                galaxies.append((x, y))
                y_has_galaxy = True
        all_missing_x.intersection_update(missing)
        if not y_has_galaxy:
            all_missing_y.append(y)

    all_missing_x = list(all_missing_x)

    distances = []

    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            dx = (abs(galaxies[i][0] - galaxies[j][0])
                  + sum([999999 for a in all_missing_x if galaxies[i][0] < a < galaxies[j][0]])
                  + sum([999999 for a in all_missing_x if galaxies[j][0] < a < galaxies[i][0]]))
            dy = (abs(galaxies[i][1] - galaxies[j][1])
                  + sum([999999 for a in all_missing_y if galaxies[i][1] < a < galaxies[j][1]])
                  + sum([999999 for a in all_missing_y if galaxies[j][1] < a < galaxies[i][1]]))
            distances.append((dx+dy, i+1, j+1))

    print(sum([d[0] for d in distances]))

if __name__ == '__main__':
    part2("input.txt")

