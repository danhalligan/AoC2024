import numpy as np
from itertools import chain


def windows(x):
    return (x[i : i + 4] for i in range(len(x) - 4 + 1))


def slices(data):
    for j in range(data.shape[1]):
        yield from windows(data[j,])


def diags(data):
    for i in range(4 - data.shape[0], data.shape[0] - 3):
        yield from windows(data.diagonal(i))


def words(data):
    return chain(slices(data), slices(data.T), diags(data), diags(np.fliplr(data)))


def match(arr):
    txt = "".join(arr)
    return txt == "XMAS" or txt == "SAMX"


def part_a(data):
    data = np.array([list(x) for x in data.lines()])
    return sum([match(x) for x in words(data)])


def match2(arr):
    for w1 in [["M", "A", "S"], ["S", "A", "M"]]:
        for w2 in [["M", "A", "S"], ["S", "A", "M"]]:
            if all(arr.diagonal() == w1) and all(np.fliplr(arr).diagonal() == w2):
                return True
    return False


def part_b(data):
    data = np.array([list(x) for x in data.lines()])
    return sum(
        [
            match2(data[i : i + 3, j : j + 3])
            for i in range(data.shape[0] - 3 + 1)
            for j in range(data.shape[1] - 3 + 1)
        ]
    )
