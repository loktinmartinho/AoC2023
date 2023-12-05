import unittest
from textwrap import dedent

from day05 import *

data = dedent("""\
            seeds: 79 14 55 13
            
            seed-to-soil map:
            50 98 2
            52 50 48
            
            soil-to-fertilizer map:
            0 15 37
            37 52 2
            39 0 15
            
            fertilizer-to-water map:
            49 53 8
            0 11 42
            42 0 7
            57 7 4
            
            water-to-light map:
            88 18 7
            18 25 70
            
            light-to-temperature map:
            45 77 23
            81 45 19
            68 64 13
            
            temperature-to-humidity map:
            0 69 1
            1 0 69
            
            humidity-to-location map:
            60 56 37
            56 93 4""")


class TestDay05(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(35, part_1(data))

    def test_find_largest_in_list_less_than_num(self):
        self.assertEqual(3, Almanac.find_largest_in_list_less_than_num(3, [1,2,3,4]))
        self.assertEqual(4, Almanac.find_largest_in_list_less_than_num(4, [1,2,3,4]))
        self.assertEqual(4, Almanac.find_largest_in_list_less_than_num(6, [1,2,3,4]))

    def test_part2(self):
        self.assertEqual(46, part_2(data))


if __name__ == '__main__':
    unittest.main()
