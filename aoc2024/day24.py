def parse(data):
    x, y = data.sections()
    wires = {}
    for line in x.lines():
        k, v = line.split(": ")
        wires[k] = int(v)

    operations = []
    for conn in y.lines():
        a, g, b, _, o = conn.split(" ")
        operations += [(a, g, b, o)]

    return wires, operations


def process(op, op1, op2):
    if op == "AND":
        return op1 & op2
    elif op == "OR":
        return op1 | op2
    elif op == "XOR":
        return op1 ^ op2


def part_a(data):
    wires, operations = parse(data)
    while operations:
        a, g, b, o = operations.pop(0)
        if a in wires and b in wires:
            wires[o] = process(g, wires[a], wires[b])
        else:
            operations += [(a, b, g, o)]

    zwires = {k: v for k, v in wires.items() if k.startswith("z")}
    zwires = [str(wires[k]) for k in sorted(zwires.keys(), reverse=True)]
    return int("".join(zwires), 2)


def bad_gates(operations):
    highest_z = sorted([o for *_, o in operations if o.startswith("z")])[-1]
    for a, g, b, o in operations:
        if o.startswith("z") and g != "XOR" and o != highest_z:
            yield o
        if g == "XOR" and not any(x.startswith(("x", "y", "z")) for x in [o, a, b]):
            yield o
        if g == "AND" and "x00" not in [a, b]:
            for a2, g2, b2, _ in operations:
                if (o == a2 or o == b2) and g2 != "OR":
                    yield o
        if g == "XOR":
            for a2, g2, b2, _ in operations:
                if (o == a2 or o == b2) and g2 == "OR":
                    yield o


def part_b(data):
    _, operations = parse(data)
    bad = set(bad_gates(operations))
    return ",".join(sorted(bad))
