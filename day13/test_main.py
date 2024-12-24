from main import part1, part2


def test_part1_example():
    assert part1("example.txt") == 480


def test_part1_input():
    assert part1("input.txt") == 29438


def test_part2_example():
    assert part2("example.txt") == 0


def test_part2_input():
    assert part2("input.txt") == 0
