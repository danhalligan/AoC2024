import re


def ints(x):
    return [int(i) for i in re.findall(r"-*\d+", x)]


def int_array(data):
    return [[*map(int, line.split())] for line in data.splitlines()]
