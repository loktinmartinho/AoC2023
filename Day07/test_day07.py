import unittest
from textwrap import dedent

from day07 import *

data = dedent("""\
        32T3K 765
        T55J5 684
        KK677 28
        KTJJT 220
        QQQJA 483""")

#         6: r'(.)\1{4,}',
#         5: r'(.)\1{3,}',
#         4: r'(?:(.)\1{1,}(.)\2{2,}|(.)\1{2,}(.)\2{1,})',
#         3: r'(.)\1{2,}',
#         2: r'(.)\1{1,}.?(.)\2{1,}',
#         1: r'(.)\1{1,}',
#         0: r'\w{5}',


class TestDay07(unittest.TestCase):

    def test_cards(self):
        self.assertEqual(Hand('AAAAA 1').type, 6)
        self.assertEqual(Hand('AAAA2 1').type, 5)
        self.assertEqual(Hand('AAA22 1').type, 4)
        self.assertEqual(Hand('AAA23 1').type, 3)
        self.assertEqual(Hand('AA223 1').type, 2)
        self.assertEqual(Hand('AA234 1').type, 1)
        self.assertEqual(Hand('A2345 1').type, 0)

    def test_part1(self):
        self.assertEqual(6440, part_1(data))

    def test_part2(self):
        self.assertEqual(None, part_2(data))


if __name__ == '__main__':
    unittest.main()
