import re
from math import lcm
from itertools import cycle

LEFT = 'L'
RIGHT = 'R'
START = 'AAA'
END = 'ZZZ'


class Node:
    def __init__(self, name: str, left: str, right: str):
        self.name = name
        self.left_str = left
        self.right_str = right

        self.left = None
        self.right = None


# class InstructionSet:
#     def __init__(self, instructions: str):
#         self.instructions = instructions


class Network:

    def __init__(self, instructions: str, nodes: list[Node]):
        self.instructions = instructions
        # self.nodes = nodes
        self.name2node = {node.name: node for node in nodes}

        for node in nodes:
            node.left = self.name2node[node.left_str]
            node.right = self.name2node[node.right_str]

    @staticmethod
    def take_a_step(current, direction):
        if direction == LEFT:
            return current.left
        elif direction == RIGHT:
            return current.right
        else:
            assert false

    def walk_to_end(self):
        steps = 0
        current = self.name2node[START]
        for instruction in cycle(self.instructions):
            # print('current ' + current.name, 'instruction ', instruction)
            if current.name == END:
                return steps
            current = self.take_a_step(current, instruction)
            steps += 1

    def walk_from_many(self):
        steps = 0
        starts = list(
            map(lambda name: self.name2node[name], filter(lambda name: name.endswith('A'), self.name2node.keys())))
        print('starts:', [start.name for start in starts])
        loopstarts, looppaths = zip(*[self.walk_until_loop(start) for start in starts])
        print('starts, paths:', loopstarts, [len(p) for p in looppaths])
        # stable_iterations = max(loopstarts) * len(self.instructions)
        return lcm(*[len(path) for path in looppaths])
        # for i, end in enumerate(ends):
        #     if all(end):
        #         return i * stable_iterations

        # i = stable_iterations
        # while True:
        #     i += 1
        #     if(i%1000000 == 0):
        #         print(i)
        #     if all([next(end) for end in ends]):
        #         return i

    def walk_until_loop(self, start: Node):
        # steps = 0
        current = start
        path = list()
        print("start at", start.name)
        while True:
            if current.name in path:
                print('loop detected: ', current.name, path)
                loopstart = path.index(current.name)
                loopnode = current
                # looplength = len(path) - loopstart

                # zs = [i for i, nodename in enumerate(path[loopstart:], loopstart) if nodename.endswith('Z')]
                # looppath = path[loopstart:]
                looppath = list()
                for instruction in self.instructions:
                    current = self.take_a_step(current, instruction)
                    looppath.append(current)

                while (current != loopnode):
                    for instruction in self.instructions:
                        current = self.take_a_step(current, instruction)
                        looppath.append(current)
                # print("Found loop:", loopstart, loopnode.name, [node.name for node in looppath])
                return loopstart, [node.name for node in looppath]
            path.append(current.name)
            # print('added ' + current.name)

            for instruction in self.instructions:
                current = self.take_a_step(current, instruction)
            # print('walked', self.instructions, 'now at', current.name)


def parse(data: str) -> Network:
    lines = data.splitlines()

    instructions = lines[0]
    nodes = list()
    for line in lines[2:]:
        match = re.match('(?P<node>\w{3}) = \((?P<left>\w{3}), (?P<right>\w{3})\)', line).groupdict()
        nodes.append(Node(match['node'], match['left'], match['right']))
    return Network(instructions, nodes)


def part_1(data: str) -> int:
    return parse(data).walk_to_end()


def part_2(data: str) -> int:
    network = parse(data)
    return network.walk_from_many()


if __name__ == '__main__':
    print('Part 1 answer: ', part_1(open('data.txt').read()))
    print('Part 2 answer: ', part_2(open('data.txt').read()))
