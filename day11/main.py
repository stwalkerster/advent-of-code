import time

def part1(input_file):
    data = [int(line) for line in open(input_file).read().split('\n')[0].split(' ') if line != ""]
    print(data)

    for i in range(0, 25):
        new_data = []

        for x in range(0, len(data)):
            if data[x] == 0:
                new_data.append(1)
            elif len(str(data[x])) % 2 == 0:
                data_str = str(data[x])
                new_data.append(int(data_str[0:len(data_str)//2]))
                new_data.append(int(data_str[len(data_str)//2:]))

            else:
                new_data.append(data[x] * 2024)


        print(new_data)
        data = new_data

        print(len(data))

def get_cache(i, blinks, cache):
    if i in cache and cache[i][blinks] is not None:
        return cache[i][blinks]
    return None

def evaluate(i, blinks, max_depth, cache):
    if blinks == max_depth:
        return 1

    c = get_cache(i, blinks, cache)
    if c is not None:
        return cache[i][blinks]

    data_str = str(i)
    str_len = len(data_str)

    if i == 0:
        c = evaluate(1, blinks + 1, max_depth, cache)
    elif str_len % 2 == 0:
        c = evaluate(int(data_str[0:str_len // 2]), blinks + 1, max_depth, cache)
        c += evaluate(int(data_str[str_len // 2:]), blinks + 1, max_depth, cache)
    else:
        c = evaluate(i * 2024, blinks + 1, max_depth, cache)

    if i not in cache:
        cache[i] = [None] * max_depth
    cache[i][blinks] = c

    return c


def part2(input_file):
    data = [int(line) for line in open(input_file).read().split('\n')[0].split(' ') if line != ""]

    # current => [] results, index by level
    cache = dict()

    max_depth = 75
    total = 0

    start = time.process_time_ns()
    for i in range(0, len(data)):
        total += evaluate(data[i], 0, max_depth, cache)
    end = time.process_time_ns()

    print(total)

if __name__ == '__main__':
    part2("input.txt")