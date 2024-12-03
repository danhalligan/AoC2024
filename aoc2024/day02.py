def inc(a, b):
    return (b - a) in [1, 2, 3]


def check(seq):
    return all(inc(a, b) for a, b in zip(seq, seq[1:]))


def part_a(data):
    data = data.int_array()
    return sum(check(seq) or check(seq[::-1]) for seq in data)


def skip1(seq):
    return (seq[:i] + seq[i + 1 :] for i in range(len(seq)))


def check_skip(seq):
    return check(seq) or any(check(subseq) for subseq in skip1(seq))


def part_b(data):
    data = data.int_array()
    return sum(check_skip(seq) or check_skip(seq[::-1]) for seq in data)
