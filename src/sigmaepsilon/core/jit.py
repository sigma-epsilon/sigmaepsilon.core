"""Optional Numba support.

The objects in this module map to their Numba equivalents if Numba is
installed. Otherwise they fall back to pure Python implementations, so that
code using them stays importable and runnable without Numba, albeit much
slower. Only the decorators and functions that have a meaningful pure Python
counterpart are covered here; features like typed containers, CUDA or
``numba.extending`` should be imported from Numba directly, guarded by
:data:`NUMBA_AVAILABLE`.

Example:
    >>> import numpy as np
    >>> from sigmaepsilon.core.jit import njit, prange
    >>> @njit(nogil=True, parallel=True)
    ... def total(a):
    ...     res = 0.0
    ...     for i in prange(len(a)):
    ...         res += a[i]
    ...     return res
    >>> float(total(np.array([1.0, 2.0, 3.0])))
    6.0

"""

from collections.abc import Callable
from typing import Any

from .thirdparty import import_package

__all__ = ["NUMBA_AVAILABLE", "jit", "njit", "prange", "vectorize"]

_numba = import_package("numba")

NUMBA_AVAILABLE: bool = _numba is not None
"""``True`` if Numba is installed, ``False`` otherwise."""


def _jit_fallback(*args: Any, **kwargs: Any) -> Callable:
    """Pure Python stand-in for :func:`numba.jit` and :func:`numba.njit`.

    It supports all the forms the Numba decorators can be used with
    (``@njit``, ``@njit(**options)``, ``@njit(signature, **options)``
    and ``njit(func, **options)``) and returns the decorated function
    unchanged. The arguments are ignored.
    """
    if args and callable(args[0]):
        return args[0]
    return lambda func: func


def _vectorize_fallback(*args: Any, **kwargs: Any) -> Callable:
    """Pure Python stand-in for :func:`numba.vectorize`.

    It is based on :class:`numpy.vectorize`. Signatures and options
    are ignored.
    """
    import numpy as np

    if args and callable(args[0]):
        return np.vectorize(args[0])
    return np.vectorize


if NUMBA_AVAILABLE:
    jit = _numba.jit
    njit = _numba.njit
    prange = _numba.prange
    vectorize = _numba.vectorize
else:
    jit = _jit_fallback
    njit = _jit_fallback
    prange = range
    vectorize = _vectorize_fallback
