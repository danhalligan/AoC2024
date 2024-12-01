from aocd.models import Puzzle
from datetime import datetime
import os.path
import yaml
from datetime import datetime


class Examples:
    """
    Class for (potentially multiple) example data sets for a given day
    Allows getting data, storing as yaml (so it can be manually edited) and
    testing against by providing a function.
    """

    def __init__(self, day=datetime.today().day):
        self.day = day
        self.file = f"tests/data/{day:02d}.yaml"
        self.puzzle = Puzzle(year=2024, day=day)
        self.data = None

    def today(self):
        return datetime.now(self.puzzle.unlock_time().tzinfo)

    def unlock_time(self):
        return self.puzzle.unlock_time()

    def available(self):
        return self.today() > self.unlock_time()

    def cached(self):
        return os.path.exists(self.file)

    def download(self):
        return [
            {"data": eg.input_data, "a": eg.answer_a, "b": eg.answer_b}
            for eg in self.puzzle.examples
        ]

    def get(self):
        if not self.data:
            if os.path.exists(self.file):
                with open(self.file) as stream:
                    self.data = yaml.safe_load(stream)
            else:
                self.data = self.download()
        return self.data

    def dump(self):
        data = self.get()
        with open(self.file, "w") as yaml_file:
            yaml_file.write(yaml.dump(data, default_style="|"))

    def test(self, part, fn):
        for example in self.get():
            if example[part] is not None:
                assert str(fn(example["data"])) == example[part]


class AOC:
    def __init__(self, day=datetime.today().day):
        self.day = day
        self.puzzle = Puzzle(year=2024, day=day)
        self.example = Examples(day)

    def get(self, example=False, number=0):
        if example:
            return self.example.get()[number]["data"]
        else:
            return self.puzzle.input_data

    def submit(self, part, answer):
        if part == "a":
            self.puzzle.answer_a = answer
        elif part == "b":
            self.puzzle.answer_b = answer
