def part1(input_file):
    data = [line.split(' ') for line in open(input_file).read().split('\n') if line != ""]
    safe = 0

    for report in data:
        if test_report(report):
            safe += 1

    print(safe)


def part2(input_file):
    data = [line.split(' ') for line in open(input_file).read().split('\n') if line != ""]
    safe = 0

    for report in data:
        safety_check = test_report(report)

        if safety_check:
            safe += 1
        else:
            for i in range(len(report)):
                working_copy = report.copy()
                working_copy.pop(i)

                if test_report(working_copy):
                    safe+=1
                    break

    print(safe)


def test_report(report):
    deltas = [int(b) - int(a) for a, b in zip(report[0:-1], report[1:])]
    delta_safety = all(1 <= abs(d) <= 3 for d in deltas)
    unidirectional = all(d < 0 for d in deltas) or all(d > 0 for d in deltas)
    return delta_safety and unidirectional


if __name__ == '__main__':
    part2("input.txt")
