import multiprocessing.dummy as mp

class Almanac:
    def __init__(self, raw_input):
        mappings = [i for i in raw_input.split('\n') if i != ""]
        self.mappings = [[int(i) for i in m.split()] for m in mappings[1::]]
        self.name = mappings[0].split()[0]

    def __repr__(self):
        return self.name + ": " + str(self.mappings)

    def map(self, value):
        for m in self.mappings:
            upper_bound = (m[1] + m[2])
            lower_bound = m[1]
            if lower_bound <= value < upper_bound:
                return m[0] + value - m[1]
        return value

def part1(inputFile):
    raw_input = open('data/day05/' + inputFile).read().split('\n\n')
    seeds = [int(s) for s in raw_input[0].split(': ')[1].split()]
    almanacs = [Almanac(i) for i in raw_input[1::]]

    locations = []

    for s in seeds:
        value = s
        for a in almanacs:
            value = a.map(value)
        locations.append(value)

    print(min(locations))

def part2_naive(inputFile):
    raw_input = open('data/day05/' + inputFile).read().split('\n\n')
    seed_data = [int(s) for s in raw_input[0].split(': ')[1].split()]

    seed_ranges = []
    for i in range(0, len(seed_data), 2):
        seed_ranges.append(range(seed_data[0], seed_data[0] + seed_data[1]))


    almanacs = [Almanac(i) for i in raw_input[1::]]

    min_locations = []

    def calc(seeds):
        locations = []
        for s in seeds:
            value = s
            for a in almanacs:
                value = a.map(value)
            locations.append(value)
        min_locations.append(min(locations))

    p = mp.Pool(22)
    p.map(calc, seed_ranges)
    p.close()
    p.join()

    print(min(min_locations))

def part2(inputFile):
    raw_input = open('data/day05/' + inputFile).read().split('\n\n')

    seed_data = [int(s) for s in raw_input[0].split(': ')[1].split()]
    seed_ranges = []
    for i in range(0, len(seed_data), 2):
        seed_ranges.append((seed_data[i], seed_data[i] + seed_data[i+1] - 1, seed_data[i], seed_data[i] + seed_data[i+1] - 1))

    almanacs = [Almanac(i) for i in raw_input[1::]]

    for a in almanacs[0::]:
        for s in seed_ranges:
            print(s)

        print("looking at almanac",a)
        for m in a.mappings:
            src_start = m[1]
            src_end = m[1] + m[2] - 1
            dst_start = m[0]
            dst_end = m[0] + m[2] - 1
            print("  mapping",src_start,'->', src_end,'==>', dst_start,'->', dst_end)

            for sr in seed_ranges.copy():
                if sr[2] < src_start < sr[3]:
                    print("    mapping",m,"start intersects seed range",sr)
                    seed_ranges.remove(sr)
                    start_delta = src_start - sr[2]
                    seed_ranges.append((sr[0], sr[0] + start_delta - 1, sr[2], sr[2] + start_delta - 1))
                    seed_ranges.append((sr[0] + start_delta, sr[1], sr[2] + start_delta, sr[3]))

            for sr in seed_ranges.copy():
                if sr[2] < src_end < sr[3]:
                    print("    mapping",m,"end intersects seed range",sr)
                    seed_ranges.remove(sr)
                    start_delta = src_end - sr[2]
                    seed_ranges.append((sr[0], sr[0] + start_delta, sr[2], sr[2] + start_delta))
                    seed_ranges.append((sr[0] + start_delta + 1, sr[1], sr[2] + start_delta + 1, sr[3]))

        for s in seed_ranges.copy():
            seed_ranges.remove(s)
            seed_ranges.append((s[0], s[1], a.map(s[2]), a.map(s[3])))


    for s in seed_ranges:
        print(s)
    print(min([s[2] for s in seed_ranges]))

if __name__ == '__main__':
    part2("input.txt")
