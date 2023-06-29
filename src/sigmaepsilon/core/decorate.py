# -*- coding: utf-8 -*-
import time
import sys
from typing import Callable, Optional
from types import ModuleType
from .thirdparty import import_package

np: Optional[ModuleType] = import_package("numpy")

__all__ = ["squeeze", "timeit", "suppress"]


def squeeze_if_array(arr):
    return np.squeeze(arr) if isinstance(arr, np.ndarray) else arr


def squeeze(default=True):
    def decorator(fnc: Callable):
        def inner(*args, squeeze: bool = default, **kwargs):
            if squeeze:
                res = fnc(*args, **kwargs)
                if isinstance(res, tuple):
                    return list(map(squeeze_if_array, res))
                elif isinstance(res, dict):
                    return {k: squeeze_if_array(v) for k, v in res.items()}
                else:
                    return squeeze_if_array(res)
            else:
                return fnc(*args, **kwargs)

        inner.__doc__ = fnc.__doc__
        return inner

    return decorator


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
