import unittest
from textwrap import dedent

from day06 import *

data = dedent("""\
        Time:      7  15   30
        Distance:  9  40  200""")


class TestDay04(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(288, part_1(data))

    def test_part2(self):
        self.assertEqual(71503, part_2(data))


if __name__ == '__main__':
    unittest.main()
