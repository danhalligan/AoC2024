from itertools import permutations


def parse(data):
    return {
        complex(i, j): v
        for j, line in enumerate(data.lines())
        for i, v in enumerate(list(line))
    }


def part_a(data):
    grid = parse(data)
    antipoles = []
    for freq in {*grid.values()} - {"."}:
        locations = [k for k in grid if grid[k] == freq]
        antipoles += [b + (b - a) for a, b in permutations(locations, 2)]

    return len(set(antipoles) & set(grid))


def part_b(data):
    grid = parse(data)
    antipoles = []
    for freq in {*grid.values()} - {"."}:
        locations = [k for k in grid if grid[k] == freq]
        for a, b in permutations(locations, 2):
            pos = b
            while pos in grid:
                antipoles += [pos]
                pos += b - a

    return len(set(antipoles))
