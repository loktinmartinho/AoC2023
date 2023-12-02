import unittest
from textwrap import dedent

from day01 import weathermachine, weathermachine2

TEST_DATA = dedent("""\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""")
TEST_DATA2 = dedent("""\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""")


class TestDay01(unittest.TestCase):
    def test_data(self):
        assert weathermachine(TEST_DATA.split('\n')) == 142

    def test_part2(self):
        # print(weathermachine2(TEST_DATA2.split('\n')))
        assert weathermachine2(TEST_DATA2.split('\n')) == 281


if __name__ == '__main__':
    unittest.main()
