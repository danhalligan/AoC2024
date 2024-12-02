from aoc2024.aoc import AOC
from aoc2024.helpers import ints


def inc(a, b):
    return (b - a) in [1, 2, 3]


def check(seq):
    return all(inc(a, b) for a, b in zip(seq, seq[1:]))


def part_a(data):
    data = [ints(x) for x in data.splitlines()]
    return sum(check(seq) or check(seq[::-1]) for seq in data)


def skip1(seq):
    return (seq[:i] + seq[i + 1 :] for i in range(len(seq)))


def check_skip(seq):
    return check(seq) or any(check(x) for x in skip1(seq))


def part_b(data):
    data = [ints(x) for x in data.splitlines()]
    return sum(check_skip(seq) or check_skip(seq[::-1]) for seq in data)
