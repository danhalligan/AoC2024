import typer
from typing import List
import importlib
from datetime import datetime
from aocd.models import Puzzle

app = typer.Typer()


@app.command()
def solve(days: List[int] = typer.Argument(None)):
    days = days if days else list(range(1, 25))
    """Solve a challenge for given days"""
    for day in days:
        day = int(day)
        module = importlib.import_module(f"aoc2024.day{day:02d}")
        puzzle = Puzzle(year=2024, day=day)
        if datetime.now(puzzle.unlock_time().tzinfo) < puzzle.unlock_time():
            continue

        print(f"--- Day {day}: {puzzle.title} ---")

        try:
            print("Part A:", getattr(module, "part_a")(puzzle.input_data))
        except AttributeError:
            print("No part A")
        try:
            print("Part B:", getattr(module, "part_b")(puzzle.input_data))
        except AttributeError:
            print("No part B")
        print()


def main():
    app()


if __name__ == "__main__":
    main()
