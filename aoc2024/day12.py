def moves(cell):
    return [cell + m for m in [-1j, -1, 1, +1j]]


def neighbours(grid, x):
    """valid neighbours of a cell"""
    return [m for m in moves(x) if m in grid]


def flood(grid, cell):
    """Flood fill from cell to find all cells in region"""
    q, seen = [cell], set()
    while q:
        cell = q.pop(0)
        seen.add(cell)
        for move in neighbours(grid, cell):
            if move not in seen and move not in q and grid[move] == grid[cell]:
                q += [move]
    return seen


def perimeter(grid, region):
    return sum(
        sum([x not in grid or grid[x] != grid[cell] for x in moves(cell)])
        for cell in region
    )


def regions(grid):
    todo = set(grid.keys())
    while todo:
        region = flood(grid, todo.pop())
        todo = todo - region
        yield region


def part_a(data):
    grid = data.grid()
    return sum(len(region) * perimeter(grid, region) for region in regions(grid))


def borders(grid, cell):
    bounds = [1, +1j, -1j, -1]
    return set(
        [x for x in bounds if cell + x not in grid or grid[cell + x] != grid[cell]]
    )


def sides(grid, region):
    sides = 0
    for cell in region:
        bounds = borders(grid, cell)
        for nb in [cell + m for m in [-1j, -1]]:
            if nb in grid and grid[nb] == grid[cell]:
                bounds -= borders(grid, nb)
        sides += len(bounds)
    return sides


def part_b(data):
    grid = data.grid()
    return sum(len(region) * sides(grid, region) for region in regions(grid))
