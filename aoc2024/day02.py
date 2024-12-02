from aoc2024.aoc import AOC
from aoc2024.helpers import ints


def inc(a, b):
    return (b - a) in [1, 2, 3]


def check(seq):
    return all(inc(*seq[i : i + 2]) for i in range(len(seq) - 1))


def valid(data):
    return [check(seq) or check(seq[::-1]) for seq in data]


def part_a(data):
    data = [ints(x) for x in data.splitlines()]
    return sum(valid(data))


def check2(seq):
    res = check(seq)
    if res:
        return True
    for i in range(len(seq)):
        if check(seq[:i] + seq[i + 1 :]):
            return True
    return False


def valid2(data):
    return [check2(seq) or check2(seq[::-1]) for seq in data]


def part_b(data):
    data = [ints(x) for x in data.splitlines()]
    return sum(valid2(data))
