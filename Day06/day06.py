import numpy as np
from math import sqrt


class Record:
    def __init__(self, time, distance):
        self.time = time
        self.distance = distance


def part_1(data: str) -> int:
    lines = data.splitlines()
    times = list(map(int, lines[0].split()[1:]))
    distances = list(map(int, lines[1].split()[1:]))
    records = [Record(t, d) for t, d in zip(times, distances)]
    total = 1
    for record in records:
        racetime = record.time
        beats = 0
        for holdtime in range(racetime):
            distance = holdtime * (racetime - holdtime)
            if distance > record.distance:
                beats += 1
        total *= beats
    return total


def part_2(data: str) -> int:
    lines = data.splitlines()
    T = int(''.join(lines[0].split()[1:]))
    D = int(''.join(lines[1].split()[1:]))

    # parabola
    # t = holdtime
    # T = racetime
    # d = racedistance
    # D = recorddistance
    # d = t(T-t) = -t^2 + Tt > D
    # -t^2 + Tt - D > 0

    # quadratic
    t0 = (T - sqrt(pow(T, 2) - 4 * D)) / 2
    t1 = (T + sqrt(pow(T, 2) - 4 * D)) / 2

    return int(t1) - int(t0)


def part_2_brute(data: str) -> int:
    lines = data.splitlines()
    times = int(''.join(lines[0].split()[1:]))
    distances = int(''.join(lines[1].split()[1:]))
    records = [Record(times, distances)]
    total = 1
    for record in records:
        racetime = record.time
        beats = 0
        for holdtime in range(racetime):
            distance = holdtime * (racetime - holdtime)
            if distance > record.distance:
                beats += 1
        total *= beats
    return total


if __name__ == '__main__':
    print(part_1(open('data.txt').read()))
    print(part_2(open('data.txt').read()))
    print(part_2_brute(open('data.txt').read()))
