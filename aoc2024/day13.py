import re


def parse(data):
    for x in data.raw.split("\n\n"):
        yield [[int(i) for i in re.findall(r"-*\d+", x)] for x in x.split("\n")]


# https://en.wikipedia.org/wiki/Cramer%27s_rule#Explicit_formulas_for_small_systems
def cramer(a, b, p):
    n1 = (p[0] * b[1] - p[1] * b[0]) / (a[0] * b[1] - a[1] * b[0])
    n2 = (p[1] * a[0] - p[0] * a[1]) / (a[0] * b[1] - a[1] * b[0])
    return n1, n2


def solve(a, b, p):
    n1, n2 = cramer(a, b, p)
    return int(3 * n1 + n2) if n1.is_integer() and n2.is_integer() else 0


def part_a(data):
    return sum(solve(*x) for x in parse(data))


def part_b(data):
    tot = 0
    for a, b, p in parse(data):
        p = [x + 10000000000000 for x in p]
        tot += solve(a, b, p)
    return tot
