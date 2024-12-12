def part1(input_file):
    data = [int(i) for i in list([line for line in open(input_file).read().split('\n') if line != ""][0])]

    disk = []
    file = 0
    for i in range(0, len(data)):
        current_file = None

        if i % 2 == 0:
            current_file = file
            file += 1

        for j in range(0, data[i]):
            disk.append(current_file)

    current_block = disk.index(None)
    current_end = len(disk) - 1

    while current_block < current_end:
        moved = False
        while not moved and current_end > current_block:
            if disk[current_end] is None:
                current_end -= 1
                continue

            disk[current_block] = disk[current_end]
            disk[current_end] = None
            moved = True


        try:
            current_block = disk.index(None)
        except ValueError:
            current_block = len(disk)

    print(sum([i * j for i, j in zip(range(0, len(disk)), disk) if j is not None]))


def part2(input_file):
    data = [int(i) for i in list([line for line in open(input_file).read().split('\n') if line != ""][0])]

    disk = []
    file = 0
    for i in range(0, len(data)):
        current_file = None

        if i % 2 == 0:
            current_file = file
            file += 1

        disk.append((current_file, data[i]))

    for f in range(current_file, -1, -1):
        file = [x for x in disk if x[0] == f][0]

        # location of old file
        old_loc = disk.index(file)

        for i in range(0, len(disk)):
            if disk[i][0] is not None:
                continue

            if disk[i][1] < file[1]:
                continue

            space = 0
            if disk[i][1] > file[1]:
                space = disk[i][1] - file[1]

            if i > old_loc:
                # don't move a file backwards|
                continue

            # remove the old file
            disk[old_loc] = (None, disk[old_loc][1])

            # insert the file into the space
            disk[i] = file

            if space > 0:
                disk.insert(i+1, (None, space))

            break

    disk_data = [[f[0] if f[0] is not None else 0 for i in range(0, f[1])] for f in disk]
    raw_disk = [block for file in disk_data for block in file]

    result = sum([i * j for i, j in zip(range(0, len(raw_disk)), raw_disk) if j is not None])
    print(result)

if __name__ == '__main__':
    # part2("example.txt")
    part2("input.txt")
