from aocd.models import Puzzle
from datetime import datetime
import os.path
import yaml


class Examples:
    """
    Class for (potentailly multiple) example data sets for a given day
    Allows getting data, storing as yaml (so it can be manually edited) and
    testing against by providing a function.
    """

    def __init__(self, day):
        self.day = day
        self.file = f"tests/data/{day:02d}.yaml"
        self.puzzle = Puzzle(year=2024, day=self.day)

    def today(self):
        return datetime.now(self.puzzle.unlock_time().tzinfo)

    def unlock_time(self):
        return self.puzzle.unlock_time()

    def available(self):
        return self.today() > self.unlock_time()

    def download(self):
        return [
            {"data": eg.input_data, "a": eg.answer_a, "b": eg.answer_b}
            for eg in self.puzzle.examples
        ]

    def dump(self):
        with open(self.file, "w") as yaml_file:
            dump = yaml.dump(self.download(), default_style="|")
            yaml_file.write(dump)

    def get(self):
        if not os.path.exists(self.file):
            self.dump()

        with open(self.file) as stream:
            return yaml.safe_load(stream)

    def test(self, part, fn):
        for example in self.get():
            if example[part] is not None:
                assert str(fn(example["data"])) == example[part]
