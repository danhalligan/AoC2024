def run(reg, prog):
    ptr = 0
    a, b, c = reg
    while ptr < len(prog):
        opcode, operand = prog[ptr], prog[ptr + 1]
        comb = {0: 0, 1: 1, 2: 2, 3: 3, 4: a, 5: b, 6: c}[operand]
        if opcode == 0:
            a //= 2**comb
        elif opcode == 1:
            b ^= operand
        elif opcode == 2:
            b = comb % 8
        elif opcode == 3 and a != 0:
            ptr = operand - 2
        elif opcode == 4:
            b ^= c
        elif opcode == 5:
            yield comb % 8
        elif opcode == 6:
            b = a // (2**comb)
        elif opcode == 7:
            c = a // (2**comb)
        ptr += 2


# equivalent of above but for specific program provided
def run2(a):
    while True:
        b = (a % 8) ^ 1
        c = a >> b
        yield (b ^ 5 ^ c) % 8
        a = a // 8
        if a == 0:
            break


def part_a(data):
    reg, prog = data.sections()
    reg = reg.grep_ints()
    prog = prog.grep_ints()
    return ",".join(map(str, run(reg, prog)))


# nightmare.
# I cheated: https://www.reddit.com/r/adventofcode/comments/1hg38ah/comment/m2icnwo/
# https://github.com/edoannunziata/jardin/blob/master/aoc24/AdventOfCode24.ipynb
def part_b(data):
    _, prog = data.sections()
    prog = prog.grep_ints()

    def solve(p, prev=0):
        if not p:
            yield prev
        else:
            for i in range(8):
                if next(run([8 * prev + i, 0, 0], prog)) == p[-1]:
                    yield from solve(p[:-1], 8 * prev + i)

    return min(solve(prog))
