import re


def ints(x):
    return [int(i) for i in re.findall(r"-*\d+", x)]
