def parse(data):
    x, y = data.sections()
    vals = {}
    for line in x.lines():
        k, v = line.split(": ")
        vals[k] = int(v)

    gates = []
    for conn in y.lines():
        a, g, b, _, o = conn.split(" ")
        gates += [[a, b, g, o]]

    return vals, gates


def part_a(data):
    vals, gates = parse(data)
    while gates:
        a, b, g, o = gates.pop(0)
        if a in vals and b in vals:
            if g == "AND":
                vals[o] = int(vals[a] & vals[b])
            elif g == "OR":
                vals[o] = int(vals[a] | vals[b])
            elif g == "XOR":
                vals[o] = int(vals[a] != vals[b])
        else:
            gates += [[a, b, g, o]]

    zvals = {k: v for k, v in vals.items() if k.startswith("z")}
    zvals = [str(vals[k]) for k in sorted(zvals.keys(), reverse=True)]
    return int("".join(zvals), 2)
