from operator import add, mul
from itertools import product
from functools import reduce


def parse_line(line):
    ans, nums = line.split(": ")
    return int(ans), [int(x) for x in nums.split()]


def test_eqn(ans, nums, ops=[add, mul]):
    for fns in product(ops, repeat=len(nums) - 1):
        tot = reduce(lambda a, b: fns[b[0]](a, b[1]), enumerate(nums[1:]), nums[0])
        if tot == ans:
            return True
    return False


def part_a(data):
    data = [parse_line(line) for line in data.lines()]
    return sum(x[0] for x in data if test_eqn(*x))


def part_b(data):
    data = [parse_line(line) for line in data.lines()]
    cat = lambda x, y: int(str(x) + str(y))
    return sum(x[0] for x in data if test_eqn(*x, ops=[add, mul, cat]))
