import numpy as np


def part_1(data: str) -> int:
    total = 0
    for line in data.splitlines():
        total += forward_history(np.array(list(map(int, line.split(' ')))))
    return total


def part_2(data: str) -> int:
    total = 0
    for line in data.splitlines():
        total += backward_history(np.array(list(map(int, line.split(' ')))))
    return total


def forward_history(x: np.array) -> int:
    levels = list()
    current = x
    levels.append(current)
    while not np.all(current == 0):
        current = current[1:] - current[:-1]
        levels.append(current)
    # print(levels)
    for i in reversed(range(len(levels))[:-1]):
        levels[i] = np.append(levels[i], levels[i][-1] + levels[i + 1][-1])
    # print(levels)
    return levels[0][-1]


def backward_history(x: np.array) -> int:
    levels = list()
    current = x
    levels.append(current)
    while not np.all(current == 0):
        current = current[1:] - current[:-1]
        levels.append(current)
    # print(levels)
    for i in reversed(range(len(levels))[:-1]):
        levels[i] = np.insert(levels[i], 0, levels[i][0] - levels[i + 1][0])
        # levels[i] = levels[i][0] - levels[i + 1][0] + levels[i]
        # print(levels)
    return levels[0][0]


if __name__ == '__main__':
    print('Part 1 answer: ', part_1(open('data.txt').read()))
    print('Part 2 answer: ', part_2(open('data.txt').read()))
