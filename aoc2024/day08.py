from itertools import permutations


def part_a(data):
    grid = data.grid()
    antipoles = []
    for freq in {*grid.values()} - {"."}:
        locations = [k for k in grid if grid[k] == freq]
        antipoles += [b + (b - a) for a, b in permutations(locations, 2)]

    return len(set(antipoles) & set(grid))


def part_b(data):
    grid = data.grid()
    antipoles = []
    for freq in {*grid.values()} - {"."}:
        locations = [k for k in grid if grid[k] == freq]
        for a, b in permutations(locations, 2):
            pos = b
            while pos in grid:
                antipoles += [pos]
                pos += b - a

    return len(set(antipoles))
