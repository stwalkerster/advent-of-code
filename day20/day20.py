import re


def part1(input_file):
    pattern = re.compile(r"^(?P<type>[&%])?(?P<label>[a-z]+) -> (?P<outputs>(?:[a-z]+(?:, )?)+)$")
    data = [pattern.match(line).groupdict() for line in open(input_file).read().split('\n') if line != ""]

    outputted_modules = []

    for d in data:
        d['outputs'] = d['outputs'].split(', ')
        outputted_modules += d['outputs']

    for d in data:
        if d['type'] == '&':
            d['state'] = dict()
            for d2 in data:
                if d['label'] in d2['outputs']:
                    d['state'][d2['label']] = 0

        if d['type'] == '%':
            d['state'] = False

        if d['type'] == '':
            d['state'] = 0

    data = {d['label']: d for d in data}
    for o in [o for o in set(outputted_modules) if o not in data]:
        data[o] = {"label": o, "type": "", "outputs": []}

    low_count = 0
    high_count = 0

    def push_the_button():
        low_count = 1
        high_count = 0

        pulse_queue = [('broadcaster', 0, 'button')]
        while len(pulse_queue) > 0:
            module_key, pulse_type, origin_key = pulse_queue.pop(0)

            #print(origin_key, "-low->" if pulse_type == 0 else '-high->', module_key)

            result = process_pulse(data[module_key], pulse_type, origin_key)
            for pulse in result:
                pulse_queue.append(pulse)
                if pulse[1] == 1:
                    high_count += 1
                else:
                    low_count += 1

        return high_count, low_count

    for i in range(1000):
        h, l = push_the_button()
        print()
        high_count += h
        low_count += l

    print("H", high_count, "L", low_count)
    print(high_count * low_count)


def process_pulse(module, type, origin):
    if type == 0:
        module['count'] += 1

    if module['type'] == '%':
        if type == 1:
            return []
        else:
            module['state'] = not module['state']

            if module['state']:
                return [(m, 1, module['label']) for m in module['outputs']]
            else:
                return [(m, 0, module['label']) for m in module['outputs']]

    if module['type'] == '&':
        module['state'][origin] = type

        return [(m, 0 if 0 not in module['state'].values() else 1, module['label']) for m in module['outputs']]

    return [(m, type, module['label']) for m in module['outputs']]


def part2(input_file):
    pattern = re.compile(r"^(?P<type>[&%])?(?P<label>[a-z]+) -> (?P<outputs>(?:[a-z]+(?:, )?)+)$")
    data = [pattern.match(line).groupdict() for line in open(input_file).read().split('\n') if line != ""]

    outputted_modules = []

    for d in data:
        d['outputs'] = d['outputs'].split(', ')
        outputted_modules += d['outputs']

    for d in data:
        if d['type'] == '&':
            d['state'] = dict()
            for d2 in data:
                if d['label'] in d2['outputs']:
                    d['state'][d2['label']] = 0
        if d['type'] == '%':
            d['state'] = False
        d["count"] = 0

    data = {d['label']: d for d in data}
    for o in [o for o in set(outputted_modules) if o not in data]:
        data[o] = {"label": o, "type": "", "outputs": [], "state": 0, "count": 0}

    def push_the_button():
        pulse_queue = [('broadcaster', 0, 'button')]
        while len(pulse_queue) > 0:
            module_key, pulse_type, origin_key = pulse_queue.pop(0)

            result = process_pulse(data[module_key], pulse_type, origin_key)
            for pulse in result:
                pulse_queue.append(pulse)

    i = 0
    while True:
        push_the_button()
        i += 1

        ds = ['gm', 'cl', 'xk', 'sn', 'lp', 'sb', 'rn', 'qm', 'db', 'mh', 'vg', 'ks' ]
        ds.reverse()

        binstr = "".join(['1' if data[d]['state'] else '0' for d in ds])

        print(str(i).zfill(5), ":", binstr, ":", int(binstr, 2), i - int(binstr, 2), ds[0], ds[-1])

        # if data['cc']['count'] == 1:
        #     print('cc', i)
        # if data['jq']['count'] == 1:
        #     print('jq', i)
        # if data['sp']['count'] == 1:
        #     print('sp', i)
        # if data['nx']['count'] == 1:
        #     print('nx', i)

        if data['rx']['count'] == 1:
            print(i)
            return

        if i == 5000:
            break

if __name__ == '__main__':
    part2("input.txt")
