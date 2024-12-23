from collections import defaultdict


def secret(x):
    x = ((x * 64) ^ x) % 16777216
    x = (int(x / 32) ^ x) % 16777216
    x = ((x * 2048) ^ x) % 16777216
    return x


def repeat(x, n=2000):
    for _ in range(n):
        x = secret(x)
    return x


def part_a(data):
    return sum([repeat(x) for x in data.grep_ints()])


def generate(x, n=2000):
    for _ in range(n):
        yield x
        x = secret(x)
    yield x


def prediction(x, n=2000):
    ints = [int(str(y)[-1]) for y in generate(x, n)]
    diffs = [b - a for a, b in zip(ints, ints[1:])]
    patterns = zip(diffs, diffs[1:], diffs[2:], diffs[3:])
    seq = {}
    for v, p in zip(ints[4:], patterns):
        if p not in seq:
            seq[p] = v
    return seq


def part_b(data):
    res = defaultdict(lambda: 0)
    for x in data.grep_ints():
        for k, v in prediction(x).items():
            res[k] += v
    return max(res.values())
