import numpy as np


def part_a(data):
    x = np.array(data.int_array())
    return sum(abs(np.sort(x[:, 0]) - np.sort(x[:, 1])))


def part_b(data):
    x = np.array(data.int_array())
    return sum(sum(x[:, 1] == i) * i for i in x[:, 0])
