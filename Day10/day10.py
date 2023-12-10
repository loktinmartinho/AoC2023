import numpy as np
from dataclasses import dataclass
import re

NORTH = 1
EAST = 2
SOUTH = 4
WEST = 8

START = 'S'

pipe2directions = {
    '|': {NORTH, SOUTH},
    '-': {EAST, WEST},
    'L': {NORTH, EAST},
    'J': {NORTH, WEST},
    '7': {SOUTH, WEST},
    'F': {SOUTH, EAST},
    '.': {}}

directions2pipe = {
    NORTH + SOUTH: '|',
    EAST + WEST: '-',
    NORTH + EAST: 'L',
    NORTH + WEST: 'J',
    SOUTH + WEST: '7',
    SOUTH + EAST: 'F'}

flipmap = {
    '|': +2,
    '-': +0,
    'L': +1,
    'J': -1,
    '7': +1,
    'F': -1,
    '.': 0,
}


@dataclass
class Target:
    x: int
    y: int
    distance: int


def part_1(data: str) -> int:
    pipes = np.array([list(line) for line in data.splitlines()])
    distances = np.ones(pipes.shape, int) * -1

    x, y = np.where(pipes == START)
    assert x.size == 1 and y.size == 1
    x = x[0]
    y = y[0]
    distances[x, y] = 0

    targets = list()

    # North
    if SOUTH in pipe2directions[pipes[x - 1, y]]:
        targets.append(Target(x - 1, y, 1))
    if EAST in pipe2directions[pipes[x, y - 1]]:
        targets.append(Target(x, y - 1, 1))
    if NORTH in pipe2directions[pipes[x + 1, y]]:
        targets.append(Target(x + 1, y, 1))
    if WEST in pipe2directions[pipes[x, y + 1]]:
        targets.append(Target(x, y + 1, 1))

    while targets:
        target = targets.pop(0)
        x = target.x
        y = target.y
        distance = target.distance

        if distances[x, y] != -1:
            continue

        distances[x, y] = distance
        pipe = pipes[x, y]
        directions = pipe2directions[pipe]

        if SOUTH in directions:
            targets.append(Target(x + 1, y, distance + 1))
        if EAST in directions:
            targets.append(Target(x, y + 1, distance + 1))
        if NORTH in directions:
            targets.append(Target(x - 1, y, distance + 1))
        if WEST in directions:
            targets.append(Target(x, y - 1, distance + 1))
    return distances.max()


def part_2(data: str) -> int:
    pipes = np.array([list(line) for line in data.splitlines()])
    distances = np.ones(pipes.shape, int) * -1

    x, y = np.where(pipes == START)
    assert x.size == 1 and y.size == 1
    x = x[0]
    y = y[0]
    distances[x, y] = 0

    targets = list()

    # Replace S with its actual pipe shape
    s_shape = 0
    if SOUTH in pipe2directions[pipes[x - 1, y]]:
        targets.append(Target(x - 1, y, 1))
        s_shape += NORTH
    if EAST in pipe2directions[pipes[x, y - 1]]:
        targets.append(Target(x, y - 1, 1))
        s_shape += WEST
    if NORTH in pipe2directions[pipes[x + 1, y]]:
        targets.append(Target(x + 1, y, 1))
        s_shape += SOUTH
    if WEST in pipe2directions[pipes[x, y + 1]]:
        targets.append(Target(x, y + 1, 1))
        s_shape += EAST

    # Trace the pipe to get its shape
    s = directions2pipe[s_shape]
    pipes[x, y] = s
    while targets:
        target = targets.pop(0)
        x = target.x
        y = target.y
        distance = target.distance

        if distances[x, y] != -1:
            continue

        distances[x, y] = distance
        pipe = pipes[x, y]
        directions = pipe2directions[pipe]

        if SOUTH in directions:
            targets.append(Target(x + 1, y, distance + 1))
        if EAST in directions:
            targets.append(Target(x, y + 1, distance + 1))
        if NORTH in directions:
            targets.append(Target(x - 1, y, distance + 1))
        if WEST in directions:
            targets.append(Target(x, y - 1, distance + 1))

    # Get a bitmask of the pipe
    pipebinary = np.zeros(distances.shape, int)
    pipebinary[np.where(distances != -1)] = 1

    # Replace non-pipe garbage with blanks
    pipes_masked = pipes
    pipes_masked[np.where(distances == -1)] = '.'

    flips = np.zeros(pipes.shape, int)

    for key, val in flipmap.items():
        flips[np.where(pipes_masked == key)] = val

    # Count the number of intersections of the ray going left out of the array
    # | counts as one intersection
    # L and 7 count as a +1/2 intersection each
    # F and J count as a -1/2 intersection each
    # The counting is this way because L7 and FJ should count as one intersection, and LJ and F7 count as zero intersections
    # Order doesn't matter because we can "untangle" the loops out (there's probably a more formal topology way to say this)
    return ((flips.cumsum(1) % 4 != 0) * (1 - pipebinary)).sum()


if __name__ == '__main__':
    print('Part 1 answer: ', part_1(open('data.txt').read()))
    print('Part 2 answer: ', part_2(open('data.txt').read()))
