from heapq import heappush, heappop
from itertools import product
from functools import cache
import re


def position(x, pad):
    return [k for k in pad.keys() if pad[k] == x][0]


def dir(m):
    return {1j: "v", 1: ">", -1j: "^", -1: "<"}[m]


def dij(graph, start):
    d, paths, q = {start: 0}, {start: set()}, []
    i = 0
    heappush(q, (0, i, start))
    seen = set()
    while q:
        s, _, p = heappop(q)
        seen.add(p)
        for m in [-1j, 1, 1j, -1]:
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


# return all paths as a string between start and end for a given keypad
# paths always end in "A"
def paths(pad, start, end):
    pad = dict(pad)
    sp = position(start, pad)
    ep = position(end, pad)
    return ["".join(p) + "A" for p in recover(dij(pad, sp), ep)]


# dictionary of best paths between all possible values on both keypads
def allpaths():
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
    ap = {}
    for pad in [numkeypad, dirkeypad]:
        for a, b in product(dict(pad).values(), repeat=2):
            ap[a, b] = paths(pad, a, b)
    return ap


def complexity(code, times=3):
    @cache
    def nbuttons(code, times):
        if times == 0:
            return len(code)

        return sum(
            min(nbuttons(path, times - 1) for path in ap[a, b])
            for a, b in zip("A" + code, code)
        )

    ap = allpaths()
    return nbuttons(code, times) * int(re.findall(r"-*\d+", code)[0])


def part_a(data):
    return sum(complexity(code) for code in data.lines())


def part_b(data):
    return sum(complexity(code, 26) for code in data.lines())
