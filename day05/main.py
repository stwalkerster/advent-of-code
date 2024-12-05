def check_update(update, rules):
    for i in range(0, len(update)):
        for r in rules:
            if not (r[0] in update and r[1] in update):
                continue

            if update[i] == r[0] and r[1] in update[:i]:
                return False

            if update[i] == r[1] and r[0] in update[i + 1:]:
                return False
    return True


def part1(input_file):
    data = [line for line in open(input_file).read().split('\n\n') if line != ""]
    rules = [[int(r) for r in line.split('|')] for line in data[0].split('\n') if line != ""]
    updates = [[int(p) for p in line.split(',')] for line in data[1].split('\n') if line != ""]

    total = 0
    for update in updates:
        if check_update(update, rules):
            total += update[len(update) // 2]

    print(total)


def reorder_update(update, rules):
    reordered = update.copy()

    # filter the rules to only the ones we care about
    local_rules = [x for x in rules if x[0] in update and x[1] in update]

    while not check_update(reordered, rules):
        for r in local_rules:

            r0index = reordered.index(r[0])
            r1index = reordered.index(r[1])

            if r1index < r0index:
                # wrong order; swap and retest
                reordered[r1index] = r[0]
                reordered[r0index] = r[1]
                break

    return reordered


def part2(input_file):
    data = [line for line in open(input_file).read().split('\n\n') if line != ""]
    rules = [[int(r) for r in line.split('|')] for line in data[0].split('\n') if line != ""]
    updates = [[int(p) for p in line.split(',')] for line in data[1].split('\n') if line != ""]

    if not all([len(x) == len(set(x)) for x in updates]):
        raise ValueError

    total = 0
    for update in updates:
        if not check_update(update, rules):
            reordered = reorder_update(update, rules)
            total += reordered[len(reordered) // 2]

    print(total)


if __name__ == '__main__':
    part2("input.txt")
