def bfs(grid, dim):
    """Breadth first search"""
    d, q = {0j: 0}, [0j]
    while q:
        p = q.pop(0)
        for n in [p + 1j, p + 1, p - 1j, p - 1]:
            if n in grid and grid[n] and n not in d:
                q.append(n)
                d[n] = d[p] + 1
                if n == complex(dim, dim):
                    return d[n]


def grid(dim, data, n):
    grid = {complex(x, y): True for x in range(dim + 1) for y in range(dim + 1)}
    for x, y in data[:n]:
        grid[complex(x, y)] = False
    return grid


def part_a(data, dim=70, n=1024):
    data = data.grep_ints(per_line=True)
    return bfs(grid(dim, data, n), dim)


def part_b(data, dim=70, n=1024):
    """Binary search"""
    data = data.grep_ints(per_line=True)

    def path(n):
        return bfs(grid(dim, data, n), dim) is not None

    low = 0
    high = len(data) - 1
    while True:
        mid = (low + high) // 2
        if low + 1 == high:
            return f"{data[low][0]},{data[low][1]}"
        elif not path(mid):
            high = mid
        elif path(low):
            low = mid
