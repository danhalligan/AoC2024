from heapq import heappush, heappop


def parse(data):
    grid = data.grid()
    (start,) = [k for k in grid.keys() if grid[k] == "S"]
    (end,) = [k for k in grid.keys() if grid[k] == "E"]
    return grid, start, end


def moves(grid, s, p, d):
    yield (s + 1000, p, d * 1j)
    yield (s + 1000, p, d * -1j)
    if grid[p + d] != "#":
        yield (s + 1, p + d, d)


def part_a(data):
    grid, start, end = parse(data)
    q, best, i = [], {}, 0
    heappush(q, (0, i, start, 1))
    best[start, 1] = 0
    while q:
        s, _, p, d = heappop(q)
        if p == end:
            return s
        for s, p, d in moves(grid, s, p, d):
            if (p, d) not in best or s < best[p, d]:
                i += 1
                heappush(q, (s, i, p, d))
                best[p, d] = s


def part_b(data):
    grid, start, end = parse(data)
    q, best, i = [], {}, 0
    heappush(q, (0, i, start, 1))
    best[start, 1] = (0, [])
    while q:
        s, _, p, d = heappop(q)

        for s, pn, dn in moves(grid, s, p, d):
            if (pn, dn) not in best or s <= best[pn, dn][0]:
                i += 1
                heappush(q, (s, i, pn, dn))
                if (pn, dn) not in best or s < best[pn, dn][0]:
                    best[pn, dn] = [s, [(p, d)]]
                else:
                    if (p, d) not in best[pn, dn][1]:
                        best[pn, dn][1] += [(p, d)]

    score = min(v[0] for k, v in best.items() if k[0] == end)
    (q,) = [v[1] for k, v in best.items() if k[0] == end and v[0] == score]
    seen = set()
    seen.add(end)
    while q:
        p, d = q.pop(0)
        seen.add(p)
        q += best[p, d][1]

    return len(set(seen))
