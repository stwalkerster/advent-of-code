import unittest
from .main import part1, part2

class AdventTests(unittest.TestCase):
    def test_part1_example(self):
        result = part1("example.txt")
        print("Part 1 Example:", result)
        self.assertEqual(result, 3)

    def test_part1_input(self):
        result = part1("input.txt")
        print("Part 1 Result:", result)
        self.assertEqual(result, 1150)

    def test_part2_example(self):
        result = part2("example.txt")
        print("Part 2 Example:", result)
        self.assertEqual(result, 6)

    def test_part2_input(self):
        result = part2("input.txt")
        print("Part 2 Result:", result)
        # self.assertLess(result, 6836)
        # self.assertGreater(result, 6601)
        self.assertEqual(result, 6738)


if __name__ == '__main__':
    unittest.main()
