import re
from math import prod


def part_a(data):
    matches = re.findall(r"mul\((-*\d+),(-*\d+)\)", data.raw)
    return sum(int(a) * int(b) for a, b in matches)


def valid(pos, dos, donts):
    a = max([x for x in dos if x < pos], default=0)
    b = max([x for x in donts if x < pos], default=-1)
    return a > b


def part_b(data):
    dos = [x.start() for x in re.finditer(r"do\(\)", data.raw)]
    donts = [x.start() for x in re.finditer(r"don't\(\)", data.raw)]

    return sum(
        prod([int(x) for x in match.groups()])
        for match in re.finditer(r"mul\((-*\d+),(-*\d+)\)", data.raw)
        if valid(match.start(), dos, donts)
    )
