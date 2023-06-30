# -*- coding: utf-8 -*-
from typing import Callable, Any

__all__ = ["InfixOperator"]


class InfixOperator:
    """
    Implements a custom Infix operator using  the 
    operators '<<', '>>' and '|'.

    Examples
    --------
    >>> x = InfixOperator(lambda x, y: x * y)
    >>> print(2 | x | 4)
    8

    >>> x = InfixOperator(lambda x, y: x + y)
    >>> print(2 << x >> 4)
    6
    """

    def __init__(self, function: Callable):
        self._function = function

    def __ror__(self, other: Any) -> "InfixOperator":
        return InfixOperator(lambda x, self=self, other=other: self._function(other, x))

    def __or__(self, other: Any) -> Any:
        return self._function(other)

    def __rlshift__(self, other: Any) -> "InfixOperator":
        return InfixOperator(lambda x, self=self, other=other: self._function(other, x))

    def __rshift__(self, other: Any) -> Any:
        return self._function(other)

    def __call__(self, value1: Any, value2: Any) -> Any:
        return self._function(value1, value2)