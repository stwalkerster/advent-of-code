def part1(inputFile):
    raw_times, raw_distance = open(inputFile).read().split('\n')[0:2]
    times = [int(i) for i in raw_times.split()[1::] if i != ""]
    distances = [int(i) for i in raw_distance.split()[1::] if i != ""]
    input_data = zip(times, distances)

    total = 1

    for race in input_data:
        winning = [(charge_time, charge_time * (race[0] - charge_time)) for charge_time in range(1, race[0]) if (charge_time * (race[0] - charge_time)) > race[1]]
        total *= len(winning)
    print(total)



def part2(inputFile):
    raw_time, raw_distance = open(inputFile).read().split('\n')[0:2]
    _, time = raw_time.split(':')
    _, distance = raw_distance.split(':')

    time = int(time.replace(' ',''))
    distance = int(distance.replace(' ',''))

    print(time, distance)
    winning = [(charge_time, charge_time * (time - charge_time)) for charge_time in range(1, time) if (charge_time * (time - charge_time)) > distance]

    print(len(winning))



if __name__ == '__main__':
    part2("input.txt")

