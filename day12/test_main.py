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


def test_part2_example():
    assert part2("example.txt") == 80


def test_part2_example2():
    assert part2("example2.txt") == 436


def test_part2_example3():
    assert part2("example3.txt") == 1206


def test_part2_example4():
    assert part2("example4.txt") == 236


def test_part2_example5():
    assert part2("example5.txt") == 368


def test_part2_input():
    assert part2("input.txt") == 911750
