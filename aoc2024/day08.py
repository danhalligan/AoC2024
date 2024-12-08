from itertools import combinations


def parse(data):
    lines = data.lines()
    return (
        {
            complex(i, j): v
            for j, line in enumerate(data.lines())
            for i, v in enumerate(list(line))
            if v != "."
        },
        complex(len(lines), len(lines[0])),
    )


def inbound(x, lim):
    return 0 <= x.real < lim.real and 0 <= x.imag < lim.imag


def part_a(data):
    grid, lim = parse(data)
    antipoles = []
    for ant in set(grid.values()):
        locations = [k for k, v in grid.items() if v == ant]
        for a, b in combinations(locations, 2):
            dist = b - a
            antipoles += [a - dist, b + dist]

    antipoles = [x for x in antipoles if inbound(x, lim)]
    return len(set(antipoles))


def part_b(data):
    grid, lim = parse(data)
    antipoles = []
    for ant in set(grid.values()):
        locations = [k for k, v in grid.items() if v == ant]
        for a, b in combinations(locations, 2):
            dist = b - a
            pos = a
            while inbound(pos, lim):
                antipoles += [pos]
                pos -= dist
            pos = b
            while inbound(pos, lim):
                antipoles += [pos]
                pos += dist

    return len(set(antipoles))
