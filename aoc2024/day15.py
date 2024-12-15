def parse(data):
    grid, inst = data.sections()
    grid = grid.grid()
    inst = "".join(inst.lines())
    inst = [{"<": -1, "^": -1j, ">": 1, "v": 1j}[x] for x in inst]
    walls = [p for p in grid.keys() if grid[p] == "#"]
    boxes = [p for p in grid.keys() if grid[p] == "O"]
    (robot,) = [p for p in grid.keys() if grid[p] == "@"]
    return walls, boxes, robot, inst


def part_a(data):
    walls, boxes, robot, inst = parse(data)
    for d in inst:
        p, to_move = robot + d, []
        while p not in walls:
            if p in boxes:
                to_move += [p]
            else:
                boxes = [x + d if x in to_move else x for x in boxes]
                robot += d
                break
            p += d

    return sum(int(x.real) + 100 * int(x.imag) for x in boxes)


def in_box(p, boxes):
    return [i for i, box in enumerate(boxes) if p in box]


def try_move(walls, boxes, d, positions, to_move):
    if any(p in walls for p in positions):
        return 0
    hits = set([i for p in positions for i in in_box(p, boxes)])
    if len(hits):
        new = [p + d for i in hits for p in boxes[i] if p + d not in positions]
        return try_move(walls, boxes, d, new, to_move | hits)
    else:
        for i in to_move:
            boxes[i] = [p + d for p in boxes[i]]
        return d


def double(x):
    return [complex(x.real * 2, x.imag), complex(x.real * 2 + 1, x.imag)]


def part_b(data):
    walls, boxes, robot, inst = parse(data)
    walls = [y for x in walls for y in double(x)]
    boxes = [double(x) for x in boxes]
    robot = double(robot)[0]

    for d in inst:
        robot += try_move(walls, boxes, d, [robot + d], set())

    return sum(int(a.real) + 100 * int(a.imag) for a, b in boxes)
