from aoc2024 import examples


for day in range(1, 25):
    x = examples.Examples(day)
    if x.available() and not x.cached():
        x.dump()
