import pytest
from main import part1, part2

def test_part1_example():
    assert part1("example.txt") == 140


def test_part1_example2():
    assert part1("example2.txt") == 772


def test_part1_example3():
    assert part1("example3.txt") == 1930


def test_part1_input():
    assert part1("input.txt") == 1488414


@pytest.mark.skip(reason="not implemented")
def test_part2_example():
    assert part2("example.txt") == 0


@pytest.mark.skip(reason="not implemented")
def test_part2_input():
    assert part2("input.txt") == 0
