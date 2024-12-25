from main import part1, part2, Robot


def test_robot_move():
    robot = Robot('p=2,4 v=2,-3')
    robot.move((11,7))
    assert robot.position == (4,1)
    robot.move((11,7))
    assert robot.position == (6,5)
    robot.move((11,7))
    assert robot.position == (8,2)
    robot.move((11,7))
    assert robot.position == (10,6)
    robot.move((11,7))
    assert robot.position == (1,3)


def test_part1_example():
    assert part1("example.txt") == 12


def test_part1_input():
    assert part1("input.txt") == 224438715


def test_part2_example():
    assert part2("example.txt") == 0


def test_part2_input():
    assert part2("input.txt") == 0
