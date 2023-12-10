import unittest
from textwrap import dedent

from day09 import *

data = dedent("""\
        0 3 6 9 12 15
        1 3 6 10 15 21
        10 13 16 21 30 45""")


class TestDay09(unittest.TestCase):

    def test_forward_history(self):
        self.assertEqual(18, forward_history(np.array(list(map(int, "0 3 6 9 12 15".split(' '))))))
        self.assertEqual(28, forward_history(np.array(list(map(int, "1 3 6 10 15 21".split(' '))))))
        self.assertEqual(68, forward_history(np.array(list(map(int, "10 13 16 21 30 45".split(' '))))))

    def test_backward_history(self):
        self.assertEqual(-3, backward_history(np.array(list(map(int, "0 3 6 9 12 15".split(' '))))))
        self.assertEqual(0, backward_history(np.array(list(map(int, "1 3 6 10 15 21".split(' '))))))
        self.assertEqual(5, backward_history(np.array(list(map(int, "10 13 16 21 30 45".split(' '))))))

    def test_part1(self):
        self.assertEqual(114, part_1(data))

    def test_part2(self):
        self.assertEqual(2, part_2(data))


if __name__ == '__main__':
    unittest.main()
