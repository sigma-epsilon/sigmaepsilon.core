# -*- coding: utf-8 -*-
from typing import Union

try:
    from collections.abc import Iterable
except ImportError:
    from collections import Iterable

__all__ = ["alphapet", "ordrange", "latinrange", "greekrange", "urange", "arabicrange"]


def alphabet(abctype: str = "latin", start: Union[str, int] = None) -> Iterable:
    """
    Generator function that yields characters from different alphabets based on
    the specified `abctype` and `start` parameters.

    Parameters
    ----------
    abctype: str, Optional
        The tipe of the alphabet. Accepted values are 'ord' or 'o' for ASCII ordinal values,
        'latin' or 'l' for Latin, 'u' for Unicode and 'greek' or 'g' for Greek letters.
        Default is 'latin'.
    start: Union[str, int], Optional
        The code of the character to start with. Default is `None`, in which case
        a character is automatically selected as the first letter of the alphabet.

    Yields
    ------
    string
        A character from the specified alphabet.

    Examples
    --------
    To generate 5 greek characters:
    >>> from sigmaepsilon.core.alphabet import alphabet
    >>> f = alphabet('greek')
    >>> characters = list(map(alphabet('greek'), range(5)))
    """
    if abctype in ("ord", "o"):
        start = 0 if start is None else start
    elif abctype in ("latin", "l"):
        start = ord("a") if start is None else start
    elif abctype == "u":
        start = ord("\u0000") if start is None else start
    elif abctype in ("greek", "g"):
        start = ord("\u03b1") if start is None else start
    else:
        raise ValueError("Invalid alphabet.")
    start = ord(start) if isinstance(start, str) else start
    while True:
        yield chr(start)
        start += 1


def ordrange(N: int = 1, **kwargs) -> Iterable:
    start = kwargs.pop("start", 0)
    if isinstance(start, str):
        start = ord(start)
    stop = kwargs.pop("stop", None)
    if stop is None or stop == start:
        stop = start + N
    return [chr(c) for c in range(start, stop)]


def latinrange(N: int = 1, **kwargs) -> Iterable:
    start = kwargs.pop("start", 97)
    stop = kwargs.pop("stop", None)
    return ordrange(N, start=start, stop=stop)


def urange(N: int = 1, **kwargs) -> Iterable:
    start = kwargs.pop("start", "\u0000")
    stop = kwargs.pop("stop", None)
    if stop is None:
        stop = start
    return ordrange(N, start=ord(start), stop=ord(stop))


def greekrange(N: int = 1) -> Iterable:
    return urange(N, start="\u03b1")


def arabicrange(N: int = 1, **kwargs) -> Iterable:
    start = kwargs.pop("start", 0)
    stop = kwargs.pop("stop", None)
    if stop is None or stop == start:
        stop = start + N
    return [str(c) for c in range(start, stop)]
