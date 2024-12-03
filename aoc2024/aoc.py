from aocd import models
from datetime import datetime
import os.path
import yaml
import re


class Data:
    """
    Access to various input data formats
    """

    def __init__(self, raw):
        self.raw = raw

    def lines(self):
        return self.raw.splitlines()

    def grep_ints(self, per_line=False):
        def ints(x):
            return [int(i) for i in re.findall(r"-*\d+", x)]

        if per_line:
            return [ints(line) for line in self.lines()]
        else:
            return ints(self.raw)

    def int_array(self):
        return [[*map(int, line.split())] for line in self.lines()]


class Example:
    """
    Store an example (data + answers)
    """

    def __init__(self, data, a=None, b=None):
        self.data = Data(data)
        self.answers = {"a": a, "b": b}

    def test(self, part, fn):
        if self.answers[part]:
            assert str(fn(self.data)) == self.answers[part]

    def as_dict(self):
        return {"data": self.data.raw, "a": self.answers["a"], "b": self.answers["b"]}

    @classmethod
    def from_class(self, x):
        return self(data=x.input_data, a=x.answer_a, b=x.answer_b)

    @classmethod
    def from_dict(self, x):
        return self(data=x["data"], a=x["a"], b=x["b"])


class Puzzle:
    """
    Represent a given day's puzzle.
    """

    def __init__(self, day=datetime.today().day):
        self._puzzle = None
        self.day = day
        self.file = f"tests/data/{day:02d}.yaml"
        self._examples = None

    def puzzle(self):
        if not self._puzzle:
            self._puzzle = models.Puzzle(year=2024, day=self.day)
        return self._puzzle

    def available(self):
        unlock = self.puzzle().unlock_time()
        today = datetime.now(unlock.tzinfo)
        return today > unlock

    def data(self):
        return Data(self.puzzle().input_data)

    def title(self):
        return self.puzzle().title

    def submit(self, part, answer):
        if part == "a":
            self.puzzle().answer_a = answer
        elif part == "b":
            self.puzzle().answer_b = answer

    def cached(self):
        return os.path.exists(self.file)

    def examples(self):
        if not self._examples:
            if not os.path.exists(self.file):
                data = [
                    {"data": x.input_data, "a": x.answer_a, "b": x.answer_b}
                    for x in self.puzzle().examples
                ]
                with open(self.file, "w") as yaml_file:
                    yaml_file.write(yaml.dump(data, default_style="|"))
            self._examples = self.__read_examples()
        return self._examples

    def test_examples(self, part, fn):
        for example in self.examples():
            if example[part] is not None:
                assert str(fn(example["data"])) == example[part]

    def __read_examples(self):
        with open(self.file) as stream:
            data = yaml.safe_load(stream)
        return [{"data": Data(x["data"]), "a": x["a"], "b": x["b"]} for x in data]
