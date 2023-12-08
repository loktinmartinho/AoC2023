import collections

import re
from functools import cmp_to_key
from collections import Counter


# class STRENGTH(Enum):
#     FIVE_OF_A_KIND = 6
#     FOUR_OF_A_KIND = 5
#     FULL_HOUSE = 4
#     THREE_OF_A_KIND = 3
#     TWO_PAIR = 2
#     TWO_OF_A_KIND = 1
#     HIGH_CARD = 0


class Hand:
    TYPEMAP = collections.OrderedDict({
        6: r'(.)\1{4,}',
        5: r'(.)\1{3,}',
        4: r'(?:(.)\1{1,}(.)\2{2,}|(.)\3{2,}(.)\4{1,})',
        3: r'(.)\1{2,}',
        2: r'(.)\1{1,}.?(.)\2{1,}',
        1: r'(.)\1{1,}',
        0: r'\w{5}',
    })

    CARDSTRENGTH = {sym: i for i, sym in enumerate(reversed('AKQJT98765432'))}

    def __init__(self, data: str):
        cards, bid = data.split(' ', 1)
        self.bid = int(bid)
        self.cards = cards

    @property
    def type(self) -> int:
        for value, pattern in self.TYPEMAP.items():
            if re.search(pattern, ''.join(sorted(self.cards))):
                return value

    @staticmethod
    def cmp(a, b) -> int:
        if a.type != b.type:
            return a.type - b.type
        for i in range(5):
            if a.cards[i] != b.cards[i]:
                return Hand.CARDSTRENGTH[a.cards[i]] - Hand.CARDSTRENGTH[b.cards[i]]


class JokerHand:
    TYPEMAP = collections.OrderedDict({
        6: r'(.)\1{4,}',
        5: r'(.)\1{3,}',
        4: r'(?:(.)\1{1,}(.)\2{2,}|(.)\3{2,}(.)\4{1,})',
        3: r'(.)\1{2,}',
        2: r'(.)\1{1,}.?(.)\2{1,}',
        1: r'(.)\1{1,}',
        0: r'\w{5}',
    })

    CARDSTRENGTH = {sym: i for i, sym in enumerate(reversed('AKQT98765432J'))}

    def __init__(self, data: str):
        cards, bid = data.split(' ', 1)
        self.bid = int(bid)
        self.cards = cards

    @property
    def type(self) -> int:
        # Replace J with the most frequent non-J letter
        result = Counter(self.cards.replace('J', ''))
        mode = max(result, key=result.get) if result else 'J'
        # print('cards:', self.cards, 'mode:', mode)
        jokers_subbed = self.cards.replace('J', mode)
        # if ('J' in self.cards):
        #     print(f"%s, J->%s, %s" % (self.cards, mode, jokers_subbed))

        for value, pattern in self.TYPEMAP.items():
            if re.search(pattern, ''.join(sorted(jokers_subbed))):
                return value

    @staticmethod
    def cmp(a, b) -> int:
        if a.type != b.type:
            return a.type - b.type
        for i in range(5):
            if a.cards[i] != b.cards[i]:
                return JokerHand.CARDSTRENGTH[a.cards[i]] - JokerHand.CARDSTRENGTH[b.cards[i]]


def part_1(data: str) -> int:
    total = 0
    for rank, hand in enumerate(sorted(map(Hand, data.splitlines()), key=cmp_to_key(Hand.cmp)), 1):
        total += (rank * hand.bid)
        # print(rank, hand.cards, hand.bid)
    return total


def part_2(data: str) -> int:
    total = 0
    for rank, hand in enumerate(sorted(map(JokerHand, data.splitlines()), key=cmp_to_key(JokerHand.cmp)), 1):
        total += (rank * hand.bid)
        print(rank, hand.cards, hand.type, hand.bid)
    return total


if __name__ == '__main__':
    print(part_1(open('data.txt').read()))
    print(part_2(open('data.txt').read()))
