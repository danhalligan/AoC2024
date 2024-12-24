from aoc2024.aoc import Puzzle
from heapq import heappush, heappop
from itertools import product
from functools import cache
import re

numkeypad = (
    (0j, "7"),
    (1, "8"),
    (2, "9"),
    (1j, "4"),
    (1 + 1j, "5"),
    (2 + 1j, "6"),
    (2j, "1"),
    (1 + 2j, "2"),
    (2 + 2j, "3"),
    (1 + 3j, "0"),
    (2 + 3j, "A"),
)

dirkeypad = (
    (1, "^"),
    (2, "A"),
    (1j, "<"),
    (1 + 1j, "v"),
    (2 + 1j, ">"),
)


def position(x, pad):
    return [k for k in pad.keys() if pad[k] == x][0]


def dir(m):
    return {1j: "v", 1: ">", -1j: "^", -1: "<"}[m]


def as_graph(g):
    return {a: b for a, b in g}


def dij(graph, start):
    d, paths, q = {start: 0}, {start: set()}, []
    i = 0
    heappush(q, (0, i, start))
    seen = set()
    while q:
        s, _, p = heappop(q)
        seen.add(p)
        for m in [1j, 1, -1j, -1]:
            n = p + m
            if n in graph and n not in seen:
                if n not in d or s + 1 < d[n]:
                    d[n] = s + 1
                    paths[n] = set([-m])
                elif n in d and s + 1 == d[n]:
                    paths[n] |= set([-m])
                i += 1
                heappush(q, (d[n], i, n))

    return paths


def recover(paths, p, path=[]):
    if not paths[p]:
        yield path
    else:
        for m in paths[p]:
            yield from recover(paths, p + m, [dir(-m)] + path)


@cache
def paths(pad, start, end):
    pad = as_graph(pad)
    sp = position(start, pad)
    ep = position(end, pad)
    return ["".join(p) + "A" for p in recover(dij(pad, sp), ep)]


def routes(pad, code):
    seqs = [list(paths(pad, a, b)) for a, b in zip("A" + code, code)]
    for seq in product(*seqs):
        yield "".join(["".join(x) if x else "" for x in seq])
        break


def filter_routes(routes):
    r = set(routes)
    best = min(len(x) for x in r)
    return [x for x in r if len(x) == best]


def best_routes(r1):
    r2 = [y for x in r1 for y in routes(dirkeypad, x)]
    return filter_routes(r2)


def abroute(a, b, n=2):
    r1 = list(paths(numkeypad, a, b))
    r1 = filter_routes(r1)
    for _ in range(n):
        r1 = best_routes(r1)
    return r1[0]


def fullroute(code, n=2):
    code = "A" + code  # always start at A
    return "".join([abroute(a, b, n=n) for a, b in zip(code, code[1:])])


def complexity(code):
    return len(fullroute(code)) * int(re.findall(r"-*\d+", code)[0])


def part_a(data):
    codes = data.lines()
    return sum(complexity(code) for code in codes)


def part_b(data):
    codes = data.lines()
    return sum(len(fullroute(code, n=18)) for code in codes)
