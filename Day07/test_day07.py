import unittest
from itertools import permutations
from textwrap import dedent

from day07 import *

data = dedent("""\
        32T3K 765
        T55J5 684
        KK677 28
        KTJJT 220
        QQQJA 483""")

FIVE_OF_A_KIND = 6
FOUR_OF_A_KIND = 5
FULL_HOUSE = 4
THREE_OF_A_KIND = 3
TWO_PAIR = 2
TWO_OF_A_KIND = 1
HIGH_CARD = 0


class TestDay07(unittest.TestCase):

    def test_hand(self):
        self.assertEqual(Hand('AAAAA 1').type, FIVE_OF_A_KIND)
        self.assertEqual(Hand('AAAA2 1').type, FOUR_OF_A_KIND)
        self.assertEqual(Hand('AAA22 1').type, FULL_HOUSE)
        self.assertEqual(Hand('AAA23 1').type, THREE_OF_A_KIND)
        self.assertEqual(Hand('AA223 1').type, TWO_PAIR)
        self.assertEqual(Hand('AA234 1').type, TWO_OF_A_KIND)
        self.assertEqual(Hand('A2345 1').type, HIGH_CARD)

    def test_jokerhands(self):
        # 5 Jokers
        self.assertEqual(JokerHand('JJJJJ 1').type, FIVE_OF_A_KIND)

        # 4 Jokers
        self.assertEqual(JokerHand('JJJJA 1').type, FIVE_OF_A_KIND)

        # 3 Jokers
        self.assertEqual(JokerHand('JJJAA 1').type, FIVE_OF_A_KIND)
        self.assertEqual(JokerHand('JJJA2 1').type, FOUR_OF_A_KIND)

        # 2 Jokers
        self.assertEqual(JokerHand('JJAAA 1').type, FIVE_OF_A_KIND)
        self.assertEqual(JokerHand('JJAA2 1').type, FOUR_OF_A_KIND)
        self.assertEqual(JokerHand('JJA23 1').type, THREE_OF_A_KIND)

        # 1 Joker
        self.assertEqual(JokerHand('JAAAA 1').type, FIVE_OF_A_KIND)
        self.assertEqual(JokerHand('JAAA2 1').type, FOUR_OF_A_KIND)
        self.assertEqual(JokerHand('JAA22 1').type, FULL_HOUSE)
        self.assertEqual(JokerHand('JAA23 1').type, THREE_OF_A_KIND)
        self.assertEqual(JokerHand('JA234 1').type, TWO_OF_A_KIND)

        # 0 Jokers
        self.assertEqual(JokerHand('AAAAA 1').type, FIVE_OF_A_KIND)
        self.assertEqual(JokerHand('AAAA2 1').type, FOUR_OF_A_KIND)
        self.assertEqual(JokerHand('AAA22 1').type, FULL_HOUSE)
        self.assertEqual(JokerHand('AAA23 1').type, THREE_OF_A_KIND)
        self.assertEqual(JokerHand('AA223 1').type, TWO_PAIR)
        self.assertEqual(JokerHand('AA234 1').type, TWO_OF_A_KIND)
        self.assertEqual(JokerHand('A2345 1').type, HIGH_CARD)

        map = {'JJJJJ': FIVE_OF_A_KIND,
               'JJJJA': FIVE_OF_A_KIND,
               'JJJAA': FIVE_OF_A_KIND,
               'JJJA2': FOUR_OF_A_KIND,
               'JJAAA': FIVE_OF_A_KIND,
               'JJAA2': FOUR_OF_A_KIND,
               'JJA23': THREE_OF_A_KIND,
               'JAAAA': FIVE_OF_A_KIND,
               'JAAA2': FOUR_OF_A_KIND,
               'JAA22': FULL_HOUSE,
               'JAA23': THREE_OF_A_KIND,
               'JA234': TWO_OF_A_KIND,
               'AAAAA': FIVE_OF_A_KIND,
               'AAAA2': FOUR_OF_A_KIND,
               'AAA22': FULL_HOUSE,
               'AAA23': THREE_OF_A_KIND,
               'AA223': TWO_PAIR,
               'AA234': TWO_OF_A_KIND,
               'A2345': HIGH_CARD}

        for hand, expected in map.items():
            for perm in permutations(hand, 5):
                # print('hand, expected:', hand, expected)
                self.assertEqual(JokerHand(''.join(perm) + ' 1').type, expected)

    def test_part1(self):
        self.assertEqual(6440, part_1(data))

    def test_part2(self):
        self.assertEqual(5905, part_2(data))


if __name__ == '__main__':
    unittest.main()
