from aocd import models
from datetime import datetime, timezone, timedelta
import os.path
import yaml
import re


class DateException(Exception):
    pass


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

    def grid(self, vtype=str):
        """
        Grid of values with complex number coordinates as dict
        """
        return {
            complex(i, j): vtype(v)
            for j, line in enumerate(self.lines())
            for i, v in enumerate(list(line))
        }


class Example:
    def __init__(self, data, a=None, b=None):
        self.data = Data(data)
        self.val = {"a": a, "b": b}

    def test_part(self, part, fn):
        if fn is not None and self.val[part]:
            return str(fn(self.data)) == self.val[part]
        return True

    def test(self, a=None, b=None):
        assert self.test_part(a, "a")
        assert self.test_part(b, "b")

    def as_dict(self):
        return {"data": self.data.raw, "a": self.val["a"], "b": self.val["b"]}

    @classmethod
    def from_class(self, x):
        return self(data=x.input_data, a=x.answer_a, b=x.answer_b)

    @classmethod
    def from_dict(self, x):
        return self(data=x["data"], a=x["a"], b=x["b"])


class Examples:
    def __init__(self, day):
        self.day = day
        self.file = f"tests/data/{day:02d}.yaml"
        self.examples = None

    def cached(self):
        return os.path.exists(self.file)

    def data(self, number):
        return self.examples[number - 1].data

    def dump(self):
        data = [x.as_dict() for x in self.examples]
        with open(self.file, "w") as yaml_file:
            yaml_file.write(yaml.dump(data, default_style="|"))

    def read(self):
        with open(self.file) as stream:
            data = yaml.safe_load(stream)
        self.examples = [Example.from_dict(x) for x in data]

    def test_part(self, part, fn):
        for example in self.examples:
            example.test_part(part, fn)

    def test(self, a=None, b=None):
        for example in self.examples:
            example.test(a=a, b=b)

    def from_class(self, data, overwrite=False):
        self.examples = [Example.from_class(x) for x in data]
        if not self.cached() or overwrite:
            self.dump()

    def load(self, puzzle=None):
        if self.cached():
            self.read()
        elif puzzle is not None:
            self.from_class(puzzle.puzzle().examples)
        else:
            raise Exception("Failed to load examples")


class Puzzle:
    def __init__(self, day=datetime.today().day):
        self.day = day
        self._puzzle = None
        if self.available():
            self.examples = Examples(day)
            self.examples.load(puzzle=self)
        else:
            raise DateException("Puzzle not available")

    def puzzle(self):
        if self._puzzle is None:
            self._puzzle = models.Puzzle(year=2024, day=self.day)
        return self._puzzle

    def unlock_time(self):
        tz = timezone(timedelta(0), "GMT")
        return datetime(2024, 12, self.day, 5, 0, tzinfo=tz)

    def available(self):
        unlock = self.unlock_time()
        today = datetime.now(unlock.tzinfo)
        return today > unlock

    def data(self, example=None):
        if example:
            try:
                return self.examples.data(example)
            except IndexError:
                print(f"Example number {example} not available")
        else:
            return Data(self.puzzle().input_data)

    def title(self):
        return self.puzzle().title

    def test(self, a=None, b=None):
        self.examples.test(a=a, b=b)

    def test_part(self, part, fn):
        self.examples.test_part(part, fn)

    def submit(self, a=None, b=None):
        if a is not None:
            self.puzzle().answer_a = a
        if b is not None:
            self.puzzle().answer_b = b
