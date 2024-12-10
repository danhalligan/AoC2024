def parse(data):
    grid = data.grid(vtype=int)
    return grid, [v for v in grid if grid[v] == 0]


def score(head, grid):
    q, reached = [head], []
    while q:
        pos = q.pop(0)
        moves = [pos + 1, pos - 1, pos + 1j, pos - 1j]
        for n in [x for x in moves if x in grid and grid[pos] + 1 == grid[x]]:
            q += [n]
            if grid[n] == 9:
                reached += [n]
    return reached


def part_a(data):
    grid, heads = parse(data)
    return sum(len(set(score(head, grid))) for head in heads)


def part_b(data):
    grid, heads = parse(data)
    return sum(len(score(head, grid)) for head in heads)
