import unittest
from textwrap import dedent

from day10 import *

simple_loop = dedent("""\
        .....
        .S-7.
        .|.|.
        .L-J.
        .....""")

complex_loop = dedent("""\
        ..F7.
        .FJ|.
        SJ.L7
        |F--J
        LJ...""")

enclose_loop = dedent("""\
        ...........
        .S-------7.
        .|F-----7|.
        .||OOOOO||.
        .||OOOOO||.
        .|L-7OF-J|.
        .|II|O|II|.
        .L--JOL--J.
        .....O.....""")

contain_loop = dedent("""\
        FF7FSF7F7F7F7F7F---7
        L|LJ||||||||||||F--J
        FL-7LJLJ||||||LJL-77
        F--JF--7||LJLJIF7FJ-
        L---JF-JLJIIIIFJLJJ7
        |F|F-JF---7IIIL7L|7|
        |FFJF7L7F-JF7IIL---7
        7-L-JL7||F7|L7F-7F7|
        L.L7LFJ|||||FJL7||LJ
        L7JLJL-JLJLJL--JLJ.L""")


class TestDay10(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(4, part_1(simple_loop))
        self.assertEqual(8, part_1(complex_loop))

    def test_part2(self):
        self.assertEqual(4, part_2(enclose_loop))
        self.assertEqual(10, part_2(contain_loop))


if __name__ == '__main__':
    unittest.main()
