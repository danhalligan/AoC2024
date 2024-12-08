import importlib
import pytest
from itertools import product
from aoc2024.aoc import Puzzle, DateException


# Test each day by importing the module and running part_a and part_b functions
# against all the examples for that day's puzzle.
# We skip tests if there is no defined function.
@pytest.mark.parametrize("day,part", product(range(1, 25), ["a", "b"]))
def test_all(day, part):
    try:
        module = importlib.import_module(f"aoc2024.day{day:02d}")
        fn = getattr(module, f"part_{part}")
        Puzzle(day).test_part(part, fn)
    except DateException:
        pytest.skip(f"Skipping day {day}: day not available")
    except AttributeError:
        pytest.skip(f"Skipping day {day}: part {part} not available")
