# -*- coding: utf-8 -*-
from typing import Optional, Union, Iterable
from types import ModuleType
from .typing import issequence
from .thirdparty import import_package

__all__ = ["float_to_str_sig", "floatformatter"]


def floatformatter(*, sig: Optional[int] = 6) -> str:
    """
    Returns a formatter, which essantially a string temapate
    ready to be formatted.

    Parameters
    ----------
    sig: int, Optional
        Number of significant digits. Default is 6.

    Returns
    -------
    string
        The string to be formatted.
        
    See also
    --------
    :func:`~sigmaepsilon.core.formatting.float_to_str_sig`
        
    Example
    --------
    Print the value of pi as a string with 4 significant digits:

    >>> from sigmaepsilon.core.formatting import floatformatter
    >>> import math
    >>> formatter = floatformatter(sig=4)
    >>> formatter.format(math.pi)
    '3.142'
    """
    return "{" + "0:.{}g".format(sig) + "}"


def float_to_str_sig(
    value: Union[float, Iterable[float]],
    *,
    sig: Optional[int] = 6,
    atol: Optional[float] = 1e-7
) -> Union[str, Iterable[str]]:
    """
    Returns a string representation of a floating point number, with
    given significant digits.

    Parameters
    ----------
    value: Union[float, Iterable[float]]
        A single value, or an iterable.

    sig: int, Optional
        Number of significant digits. Default is 6.

    atol: float, Optional
        Floating point tolerance. Values smaller than this
        in the absolute sense are treated as zero. Default is 1e-7.

    Returns
    -------
    Union[str, Iterable[str]]
        String representation of the provided input.
        
    See also
    --------
    :func:`~sigmaepsilon.core.formatting.floatformatter`

    Example
    --------
    Print the value of pi as a string with 4 significant digits:

    >>> from sigmaepsilon.core.formatting import float_to_str_sig
    >>> import math
    >>> float_to_str_sig(math.pi, sig=4)
    '3.142'
    """
    if not issequence(value):
        if atol is not None:
            if abs(value) < atol:
                value = 0.0
        return floatformatter(sig=sig).format(value)
    else:
        np: Optional[ModuleType] = import_package("numpy")
        if not np:
            raise ImportError("You need numpy for this.")
        value = np.array(value)
        if atol is not None:
            inds = np.where(np.abs(value) < atol)[0]
            value[inds] = 0.0
        formatter = floatformatter(sig=sig)

        def f(v):
            return formatter.format(v)

        return list(map(f, value))
