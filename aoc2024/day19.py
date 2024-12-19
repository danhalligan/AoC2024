from functools import cache


def parse(data):
    towels, patterns = data.sections()
    return tuple(towels.raw.split(", ")), patterns.lines()


@cache
def find_match(p, towels):
    if not len(p):
        return True
    else:
        return sum(find_match(p[len(t) :], towels) for t in towels if p.startswith(t))


def part_a(data):
    towels, patterns = parse(data)
    return sum(find_match(p, towels) > 0 for p in patterns)


def part_b(data):
    towels, patterns = parse(data)
    return sum(find_match(p, towels) for p in patterns)
