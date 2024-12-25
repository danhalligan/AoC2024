from heapq import heappush, heappop
from itertools import product
from functools import cache
import re
from math import inf
from collections import Counter, defaultdict

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


@cache
def route(pad, code):
    seq = [paths(pad, a, b)[0] for a, b in zip("A" + code, code)]
    return "".join(["".join(x) if x else "" for x in seq])


def filter_routes(routes):
    best = min(len(x) for x in routes)
    return [x for x in routes if len(x) == best]


def abroute(a, b, n=2):
    r = filter_routes(paths(numkeypad, a, b))
    for _ in range(n):
        r = filter_routes([route(dirkeypad, x) for x in r])
    return r[0]


def fullroute(code, n=2):
    return "".join([abroute(a, b, n=n) for a, b in zip("A" + code, code)])


def complexity(code):
    return len(fullroute(code)) * int(re.findall(r"-*\d+", code)[0])


def part_a(data):
    codes = data.lines()
    return sum(complexity(code) for code in codes)


@cache
def route2(pad, code):
    # breakpoint()
    seq = [paths(pad, a, b)[0] for a, b in zip("A" + code, code)]
    return ["".join(x) if x else "" for x in seq]


def clen(route):
    return sum(len(k) * v for k, v in route.items())


def iterate(r):
    r2 = []
    best = inf
    for x in r:
        rx = defaultdict(lambda: 0)
        for k, v in x.items():
            for y in route2(dirkeypad, k):
                rx[y] += v
        best = min(best, clen(rx))
        r2 += [rx]
    return [x for x in r2 if clen(x) == best]


def fullroute2(code, n):
    tot = 0
    for a, b in zip("A" + code, code):
        r = filter_routes(paths(numkeypad, a, b))
        r = [dict(Counter([x])) for x in r]
        for _ in range(n):
            r = iterate(r)
        tot += sum(len(k) * v for k, v in r[0].items())
    return tot


# def part_b(data):
#     codes = data.lines()
#     return sum(len(fullroute(code, n=4)) for code in codes)


def complexity2(code, n):
    return fullroute2(code, n=n) * int(re.findall(r"-*\d+", code)[0])


def part_b(data):
    codes = data.lines()
    tot = 0
    for code in codes:
        tot += complexity2(code, 3)
    return tot
    # return 306335137543664
