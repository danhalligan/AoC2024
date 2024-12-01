from aoc2024 import aoc


for day in range(1, 25):
    x = aoc.Examples(day)
    if x.available() and not x.cached():
        x.dump()
