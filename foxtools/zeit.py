import datetime
import time


def time_now():
    return datetime.datetime.now()


class Stopwatch:
    def __init__(self):
        self.start = 0.0
        self.ende = 0.0

    def __enter__(self):
        self.start = time.perf_counter()
        self.ende = self.start
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.ende = time.perf_counter()

    def elapsed(self):
        if self.ende == 0.0:
            return time.perf_counter() - self.start
        return self.ende - self.start

    def __call__(self):
        return self.elapsed()


def timer(func, *args, **kwargs):
    start = time.perf_counter()
    func(*args, **kwargs)
    return time.perf_counter() - start
