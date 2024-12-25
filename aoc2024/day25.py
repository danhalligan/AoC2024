def part_a(data):
    panels = data.sections()
    panels = [x.grid() for x in panels]
    locks, keys = [], []
    for panel in panels:
        lock = panel[complex(0, 0)] == "#"
        heights = [
            sum(panel[complex(j, i)] == "#" for i in range(7)) - 1 for j in range(5)
        ]
        if lock:
            locks += [heights]
        else:
            keys += [heights]

    return sum(
        [all(x + y <= 5 for x, y in zip(lock, key)) for key in keys for lock in locks]
    )
