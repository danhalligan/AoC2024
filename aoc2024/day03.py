import re
from math import prod


def part_a(data):
    data = data.raw
    matches = re.findall(r"mul\((-*\d+),(-*\d+)\)", data)
    return sum(int(a) * int(b) for a, b in matches)


def valid(pos, dos, donts):
    a = max([x for x in dos if x < pos], default=0)
    b = max([x for x in donts if x < pos], default=-1)
    return a > b


def part_b(data):
    data = data.raw
    dos = [x.start() for x in re.finditer(r"do\(\)", data)]
    donts = [x.start() for x in re.finditer(r"don't\(\)", data)]

    return sum(
        prod([int(x) for x in match.groups()])
        for match in re.finditer(r"mul\((-*\d+),(-*\d+)\)", data)
        if valid(match.start(), dos, donts)
    )
