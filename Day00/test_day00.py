import unittest
from textwrap import dedent

from day00 import *

data = dedent("""\
        """)


class TestDay00(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(None, part_1(data))

    def test_part2(self):
        self.assertEqual(None, part_2(data))


if __name__ == '__main__':
    unittest.main()
