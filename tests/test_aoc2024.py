import importlib
import pytest
from itertools import product
from aoc2024 import examples


# Test each day by importing the module and running part_a and part_b functions
# against all the examples for that day's puzzle.
# We skip tests if there is no defined function.
@pytest.mark.parametrize("day,part", product(range(1, 25), ["a", "b"]))
def test_all(day, part):
    try:
        module = importlib.import_module(f"aoc2024.day{day:02d}")
        fn = getattr(module, f"part_{part}")
    except AttributeError:
        pytest.skip(f"Skipping day {day}, part {part}")

    examples.Examples(day).test(part, fn)
