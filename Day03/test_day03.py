import unittest
from textwrap import dedent

from day03 import *

data = dedent("""\
    467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598..""")


class TestDay03(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(4361, part_1(data))

    def test_part2(self):
        self.assertEqual(467835, part_2(data))


if __name__ == '__main__':
    unittest.main()
