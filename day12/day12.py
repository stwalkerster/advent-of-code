# Count number of ?s in line (n)
# iterate from 0 to 2^n, convert i to binary
# substitute binary bits into string
# test against second data format

def part1(input_file):
    data = [line for line in open(input_file).read().split('\n') if line != ""]

    grand_total = 0

    for line in data:
        bitwise, countwise = line.split(' ')

        print(bitwise, countwise)

        needed_sections = [int(x) for x in countwise.split(',')]
        total = 0

        bitwise_parts = bitwise.split('?')
        n = len(bitwise_parts) - 1
        for i in range(pow(2, n)):
            bin_string = format(i, 'b').zfill(n)

            possible_layout = ''.join([c[0]+c[1] for c in zip(bitwise_parts, list(bin_string))]) + bitwise_parts[-1]

            sections = []
            in_section = False
            section_count = 0
            for c in possible_layout:
                if c == '#' or c == '1':
                    in_section = True
                    section_count += 1
                else:
                    if in_section == True:
                        in_section = False
                        sections.append(section_count)
                        section_count = 0

            if in_section == True:
                sections.append(section_count)

            if needed_sections == sections:
                total += 1
                #print("   ", possible_layout, sections, "MATCHES!")
            else:
                #print("   ", possible_layout, sections)
                pass
        grand_total += total
    print(grand_total)



def part2(input_file):
    data = [line for line in open(input_file).read().split('\n') if line != ""]


if __name__ == '__main__':
    part1("input.txt")
