import re
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

    def walk_to_end(self):
        steps = 0
        current = self.name2node[START]
        for instruction in cycle(self.instructions):
            # print('current ' + current.name, 'instruction ', instruction)
            if current.name == END:
                return steps
            if instruction == LEFT:
                current = current.left
            elif instruction == RIGHT:
                current = current.right
            else:
                assert false
            steps += 1


def parse(data: str) -> Network:
    lines = data.splitlines()

    instructions = lines[0]
    nodes = list()
    for line in lines[2:]:
        match = re.match('(?P<node>\w{3}) = \((?P<left>\w{3}), (?P<right>\w{3})\)', line).groupdict()
        nodes.append(Node(match['node'], match['left'], match['right']))
    return Network(instructions, nodes)


def part_1(data: str) -> int:
    network = parse(data)
    print(network)
    return network.walk_to_end()


def part_2(data: str) -> int:
    total = 0


if __name__ == '__main__':
    print('Part 1 answer: ', part_1(open('data.txt').read()))
    print('Part 2 answer: ', part_2(open('data.txt').read()))
