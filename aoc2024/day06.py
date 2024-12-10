def parse(data):
    grid = data.grid()
    start = [k for k, v in grid.items() if v == "^"][0]
    return grid, start


def visit(grid, start):
    visited = {start: True}
    pos, direction = start, -1j
    while pos + direction in grid.keys():
        if grid[pos + direction] == "#":
            direction *= 1j
        pos += direction
        visited[pos] = True
    return visited


def part_a(data):
    return len(visit(*parse(data)).keys())


# for a loop we need to visit a pos in the same direction as we did previously
def try_obstacle(grid, start, pos):
    grid[pos] = "#"
    pos, direction = start, -1j
    visited = {(start, direction): True}
    while pos + direction in grid.keys():
        if grid[pos + direction] == "#":
            direction *= 1j
        else:
            pos += direction
            if (pos, direction) in visited:
                return True
            visited[(pos, direction)] = True
    return False


def part_b(data):
    grid, start = parse(data)
    visited = visit(grid, start)
    locations = list(visited.keys())[1:]
    return sum(try_obstacle(grid.copy(), start, pos) for pos in locations)
