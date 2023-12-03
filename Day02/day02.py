import re
from collections import defaultdict
from math import prod


def part_1(data: str, acceptable=defaultdict(int, {'red': 12, 'green': 13, 'blue': 14})):
    total = 0

    for line in data.splitlines():
        gamemax = defaultdict(int)
        gameid, game = line.split(': ', 1)
        id = int(re.match(r"Game (\d+)", gameid).groups(1)[0])
        for pull in game.split('; '):
            for k, v in parse_pull(pull).items():
                if v > gamemax[k]:
                    gamemax[k] = v

        ok = True
        for color in gamemax.keys():
            if gamemax[color] > acceptable[color]:
                ok = False
                # print('not ok: ', color, gamemax)
        if ok:
            # print('ok: ', id)
            total += id
    return total


def part_2(data: str):
    total = 0

    for line in data.splitlines():
        gamemax = defaultdict(int)
        gameid, game = line.split(': ', 1)
        id = int(re.match(r"Game (\d+)", gameid).groups(1)[0])
        for pull in game.split('; '):
            for k, v in parse_pull(pull).items():
                if v > gamemax[k]:
                    gamemax[k] = v

        total += prod(gamemax.values())
    return total


def parse_pull(pull):
    ret = dict()
    for colorset in pull.split(', '):
        num, color = colorset.split(' ', 1)
        ret[color] = int(num)
    return ret


if __name__ == '__main__':
    print(part_1(open('data.txt').read()))
    print(part_2(open('data.txt').read()))
