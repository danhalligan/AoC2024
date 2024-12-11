from collections import defaultdict


# Order doesn't matter, we just need to count how many of each stone type we
# have...
def update(stones):
    new = defaultdict(int)
    for stone, count in stones.items():
        if stone == 0:
            new[1] += count
        elif len(str(stone)) % 2 == 0:
            x = str(stone)
            new[int(x[0 : len(x) // 2])] += count
            new[int(x[len(x) // 2 :])] += count
        else:
            new[stone * 2024] += count
    return new


def solve(data, n):
    stones = defaultdict(int)
    for stone in data:
        stones[stone] += 1
    for _ in range(n):
        stones = update(stones)
    return sum(stones.values())


def part_a(data):
    return solve(data.grep_ints(), 25)


def part_b(data):
    return solve(data.grep_ints(), 75)
