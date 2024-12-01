import numpy as np
from .helpers import ints


def parse(data):
    return np.array([ints(x) for x in data.splitlines()])


def part_a(data):
    x = parse(data)
    return sum(abs(np.sort(x[:, 0]) - np.sort(x[:, 1])))


def part_b(data):
    x = parse(data)
    return sum(sum(x[:, 1] == i) * i for i in x[:, 0])
