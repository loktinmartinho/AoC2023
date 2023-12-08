import unittest
from textwrap import dedent

from day08 import *

data1 = dedent("""\
        RL

        AAA = (BBB, CCC)
        BBB = (DDD, EEE)
        CCC = (ZZZ, GGG)
        DDD = (DDD, DDD)
        EEE = (EEE, EEE)
        GGG = (GGG, GGG)
        ZZZ = (ZZZ, ZZZ)""")

data2 = dedent("""\
        LLR
        
        AAA = (BBB, BBB)
        BBB = (AAA, ZZZ)
        ZZZ = (ZZZ, ZZZ)""")


class TestDay08(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(2, part_1(data1))
        self.assertEqual(6, part_1(data2))

    def test_part2(self):
        self.assertEqual(None, part_2(data1))


if __name__ == '__main__':
    unittest.main()
