from operator import add, mul
from itertools import product
from functools import reduce


def parse_line(line):
    ans, nums = line.split(": ")
    return int(ans), [int(x) for x in nums.split()]


def solve(nums, fns):
    return reduce(lambda a, b: fns[b[0]](a, b[1]), enumerate(nums[1:]), nums[0])


def test_eqn(ans, nums, ops=[add, mul]):
    return any(solve(nums, fns) == ans for fns in product(ops, repeat=len(nums) - 1))


def cat(a, b):
    return int(str(a) + str(b))


def part_a(data):
    data = [parse_line(line) for line in data.lines()]
    return sum(x[0] for x in data if test_eqn(*x))


def part_b(data):
    data = [parse_line(line) for line in data.lines()]
    return sum(x[0] for x in data if test_eqn(*x, ops=[add, mul, cat]))
