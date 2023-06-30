# -*- coding: utf-8 -*-
import time
import sys
from typing import Callable

__all__ = ["timeit", "suppress"]


def timeit(fnc: Callable) -> Callable:
    """
    A simple decorator to measure execution time of a function.
    """

    def inner(*args, **kwargs):
        t0 = time.time()
        fnc(*args, **kwargs)
        t1 = time.time()
        return t1 - t0

    return inner


def suppress(fnc: Callable) -> Callable:
    """
    Decorator that wraps a function to temporarily suppress the standard output
    for the time of execution.
    """

    def inner(*args, **kwargs):
        original_stdout = sys.stdout
        sys.stdout = None
        res = fnc(*args, **kwargs)
        sys.stdout = original_stdout
        return res

    return inner
