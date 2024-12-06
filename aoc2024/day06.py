def parse(data):
    grid = {
        complex(i, j): v
        for j, line in enumerate(data.lines())
        for i, v in enumerate(list(line))
    }
    start = [k for k, v in grid.items() if v == "^"][0]
    return grid, start


def visit(grid, start):
    visited = {start: True}
    pos, dir = start, -1j
    while pos + dir in grid.keys():
        if grid[pos + dir] == "#":
            dir *= 1j
        pos += dir
        visited[pos] = True
    return visited


def part_a(data):
    return len(visit(*parse(data)).keys())


# for a loop we need to visit a pos in the same direction as we did previously
def try_obstacle(grid, start, pos):
    grid[pos] = "#"
    pos, dir = start, -1j
    visited = {(start, dir): True}
    while pos + dir in grid.keys():
        if grid[pos + dir] == "#":
            dir *= 1j
        else:
            pos += dir
            if (pos, dir) in visited:
                return True
            else:
                visited[(pos, dir)] = True
    return False


def part_b(data):
    grid, start = parse(data)
    visited = visit(grid, start)
    locations = list(visited.keys())[1:]
    return sum(try_obstacle(grid.copy(), start, pos) for pos in locations)
