import time

import foxtools.zeit as zeit


def test_stopwatch_context_manager():
    with zeit.Stopwatch() as timer:
        time.sleep(0.01)
    assert timer.elapsed() >= 0.01
    assert timer() >= 0.01


def test_timer_returns_elapsed_seconds():
    def sample(value):
        time.sleep(0.01)
        return value * 2

    elapsed = zeit.timer(sample, 21)
    assert elapsed >= 0.01
