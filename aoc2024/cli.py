import typer
from typing import List
import importlib
from aoc2024.aoc import Puzzle, DateException

app = typer.Typer()


@app.command()
def solve(days: List[int] = typer.Argument(None)):
    days = days if days else range(1, 26)
    """Solve a challenge for given days"""
    for day in days:
        day = int(day)
        module = importlib.import_module(f"aoc2024.day{day:02d}")
        try:
            puzzle = Puzzle(day=day)
        except DateException:
            continue

        print(f"--- Day {day}: {puzzle.title()} ---")
        for part in ["a", "b"]:
            try:
                result = getattr(module, f"part_{part}")(puzzle.data())
                print(f"Part {part}:", result)
            except AttributeError:
                print(f"No part {part}")
        print()


def main():
    app()
