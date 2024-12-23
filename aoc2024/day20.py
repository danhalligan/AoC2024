def parse(data):
    grid = data.grid()
    (start,) = [k for k, v in grid.items() if v == "S"]
    (end,) = [k for k, v in grid.items() if v == "E"]
    return grid, start, end


def flood(grid, start, end):
    d, q = {start: [start]}, [start]
    while q:
        p = q.pop(0)
        for n in [p + 1j, p + 1, p - 1j, p - 1]:
            if n in grid and grid[n] != "#" and n not in d:
                q.append(n)
                d[n] = d[p] + [n]
                if n == end:
                    return d[n]


def manhattan(x, y):
    return abs((x - y).real) + abs((x - y).imag)


def find_cheats(grid, start, end, size, lim=100):
    path = flood(grid, start, end)
    for i in range(len(path)):
        for j in range(i, len(path)):
            d = manhattan(path[i], path[j])
            yield d <= size and j - i - d >= lim


def part_a(data, lim):
    grid, start, end = parse(data)
    return sum(find_cheats(grid, start, end, 2, lim=lim))


def part_b(data, lim):
    grid, start, end = parse(data)
    return sum(find_cheats(grid, start, end, 20, lim=lim))
