import re


def weathermachine(lines):
    total = 0
    for line in lines:
        first = int(re.search(r'^\D*(\d)', line).group(1))
        last = int(re.search(r'(\d)\D*$', line).group(1))
        total += 10 * first + last
    return total


def weathermachine2(lines):
    total = 0
    nummap = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }

    for line in lines:
        # matches = re.search(
        #     r'(1|2|3|4|5|6|7|8|9|(?:one)|(?:two)|(?:three)|(?:four)|(?:five)|(?:six)|(?:seven)|(?:eight)|(?:nine)).*(1|2|3|4|5|6|7|8|9|(?:one)|(?:two)|(?:three)|(?:four)|(?:five)|(?:six)|(?:seven)|(?:eight)|(?:nine))',
        #     line)
        # if not matches:
        #     print('---', line)
        #     continue
        # groups = matches.groups()
        # first = nummap[groups[0]]
        # # print(first)
        # # print(line[::-1])
        # # matches = re.search(r'(enin|thgie|neves|xis|evif|ruof|eerht|owt|eno)', line[::-1]).groups()
        # # print(matches)
        # last = nummap[groups[1]]
        # print(10 * first + last, first, last, line[:matches.span()[0]], line[matches.span()[0]:matches.span()[1]], line[matches.span()[1]:])
        # total += 10 * first + last

        matches = re.finditer(
            r'(?=(1|2|3|4|5|6|7|8|9|(?:one)|(?:two)|(?:three)|(?:four)|(?:five)|(?:six)|(?:seven)|(?:eight)|(?:nine)))',
            line)
        nums = [nummap[match.group(1)] for match in matches]
        total += 10 * nums[0] + nums[-1]
    return total


if __name__ == '__main__':
    print(weathermachine(open('data.txt').read().split('\n')))
    print(weathermachine2(open('data.txt').read().split('\n')))
