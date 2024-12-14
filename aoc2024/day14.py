def parse(data):
    for x, y, vx, vy in data.grep_ints(per_line=True):
        yield (x, y), (vx, vy)


def view(robots, dx, dy):
    for y in range(dy):
        for x in range(dx):
            tot = 0
            for (px, py), _ in robots:
                if x == px and y == py:
                    tot += 1
            if tot == 0:
                print(".", end="")
            else:
                print(tot, end="")
        print()


def count_robots(robots, rx, ry):
    return sum(x == px and y == py for (px, py), _ in robots for x in rx for y in ry)


def move(robots, t, dx, dy):
    for _ in range(t):
        for i, ((x, y), (vx, vy)) in enumerate(robots):
            robots[i] = (((x + vx) % dx, (y + vy) % dy), (vx, vy))
    return robots


def safety(robots, dx, dy):
    tot = 1
    for rx in [range(dx // 2), range(dx // 2 + 1, dx)]:
        for ry in [range(dy // 2), range(dy // 2 + 1, dy)]:
            tot *= count_robots(robots, rx, ry)
    return tot


def has_cluster(robots, n, dx, dy):
    g = [[False] * dx for _ in range(dy)]
    for (x, y), _ in robots:
        g[y][x] = True
    for y in range(dy - n):
        for x in range(dx - n):
            if all(g[iy][ix] for ix in range(x, x + n) for iy in range(y, y + n)):
                return True
    return False


def part_a(data, dx=101, dy=103):
    robots = list(parse(data))
    robots = move(robots, 100, dx, dy)
    return safety(robots, dx, dy)


def part_b(data, dx=101, dy=103):
    robots = list(parse(data))
    for i in range(10_000):
        robots = move(robots, 1, dx, dy)
        if has_cluster(robots, 3, dx, dy):
            return i + 1
