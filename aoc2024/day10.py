def parse(data):
    grid = {
        complex(i, j): int(v)
        for j, line in enumerate(data.lines())
        for i, v in enumerate(list(line))
    }
    return grid, [v for v in grid if grid[v] == 0]


def score(head, grid):
    q, reached, rating = [head], set(), 0
    while q:
        pos = q.pop(0)
        moves = [pos + 1, pos - 1, pos + 1j, pos - 1j]
        for n in [x for x in moves if x in grid and grid[pos] + 1 == grid[x]]:
            q += [n]
            if grid[n] == 9:
                reached.add(n)
                rating += 1
    return {"score": len(reached), "rating": rating}


def part_a(data):
    grid, heads = parse(data)
    return sum(score(head, grid)["score"] for head in heads)


def part_b(data):
    grid, heads = parse(data)
    return sum(score(head, grid)["rating"] for head in heads)
