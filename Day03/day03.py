import numpy as np

EMPTY = '.'
GEAR = '*'


def part_1(data: str):
    total = 0
    ewpad = [EMPTY + line + EMPTY for line in data.splitlines()]
    w = len(ewpad[0])
    pad = [EMPTY * w] + ewpad + [EMPTY * w]

    start = None
    end = None
    for i in range(len(pad)):
        for j in range(len(pad[i])):
            if not start and pad[i][j].isdigit():
                start = [i, j]
            elif start and not pad[i][j].isdigit():
                end = [i, j - 1]
                num = int(pad[i][start[1]:end[1] + 1])
                # top_left = [start[0]-1, start[1]-1]
                # bottom_right = [end[0]+1, end[1]+1]
                top = start[0] - 1
                bottom = end[0] + 1
                left = start[1] - 1
                right = end[1] + 1

                valid = False
                for k in range(top, bottom + 1):
                    for l in range(left, right + 1):
                        targ = pad[k][l]
                        if not (targ.isdigit() or targ == EMPTY):
                            valid = True
                if valid:
                    total += num
                start = None
                end = None
    return total


def part_2(data: str):
    total = 0
    ewpad = [EMPTY + line + EMPTY for line in data.splitlines()]
    w = len(ewpad[0])
    data = [EMPTY * w] + ewpad + [EMPTY * w]

    # data = data.splitlines()

    grouptopart = list([None])
    groupnums = np.zeros((len(data), len(data[0])), int)

    start = None
    end = None
    for i in range(len(data)):
        for j in range(len(data[i])):
            if not start and data[i][j].isdigit():
                start = [i, j]
            elif start and not data[i][j].isdigit():
                end = [i, j - 1]
                groupnums[start[0]:end[0] + 1, start[1]:end[1] + 1] = len(grouptopart)
                grouptopart.append(int(data[i][start[1]:end[1] + 1]))

                start = None
                end = None

    for i in range(len(data)):
        for j in range(len(data[i])):
            if (data[i][j] == GEAR):
                adjacent_parts = set(groupnums[i - 1:i + 2, j - 1:j + 2].flatten())
                adjacent_parts.remove(0)
                if len(adjacent_parts) == 2:
                    a = adjacent_parts.pop()
                    b = adjacent_parts.pop()
                    total += grouptopart[a] * grouptopart[b]
    return total


if __name__ == '__main__':
    print(part_1(open('data.txt').read()))
    print(part_2(open('data.txt').read()))
