import numpy as np
import re
import itertools


def part_1(data: str):
    total = 0
    for line in data.splitlines():
        m = re.match(r'Card +(\d+): ', line)
        winnersstr, ticketsstr = line[m.span()[1]:].split('|')
        winners = set(map(int, winnersstr.split()))
        tickets = set(map(int, ticketsstr.split()))
        total += eval_winners(winners, tickets)
    return total


def count_winners(winners: set[int], tickets: set[int]) -> int:
    return sum(ticket in winners for ticket in tickets)


def eval_winners(winners: set[int], tickets: set[int]) -> int:
    n = count_winners(winners, tickets)
    return pow(2, n - 1) if n > 0 else 0


def part_2(data: str):
    num_cards = [1] * len(data.splitlines())
    for i, line in enumerate(data.splitlines()):
        m = re.match(r'Card +(\d+): ', line)
        winnersstr, ticketsstr = line[m.span()[1]:].split('|')
        winners = set(map(int, winnersstr.split()))
        tickets = set(map(int, ticketsstr.split()))
        cards = num_cards[i]
        for j in range(count_winners(winners, tickets)):
            num_cards[i+1+j] += cards
    return sum(num_cards)


if __name__ == '__main__':
    print(part_1(open('data.txt').read()))
    print(part_2(open('data.txt').read()))
