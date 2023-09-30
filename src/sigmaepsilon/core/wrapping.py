# -*- coding: utf-8 -*-
from typing import Any

__all__ = ["Wrapper", "wrapper", "customwrapper", "wrap"]

NoneType = type(None)


class Wrapper:
    """
    Wrapper base class that makes it easy (and safe) to extend other objects.
    Based on the provided arguments at initialization, the wrapper either
    
    (a) wraps an existing object at object creation provided as a keyword
        argument with `Wrapper.wrapkey`
    (b) wraps an existing object at object creation if it is a positional
        argument and an instance of `Wrapper.wraptype`
    (b) wraps the object Wrapper.wraptype(*args, **kwargs) if
        `Wrapper.wraptype` is not `None`
        
    The attributes and methods of the wrapped instance are all accessible
    through the wrapper.
    
    Using a wrapper is a good idea if you want to easily extend the functionality
    provided by a class of an external library without having to worry about shadowing
    an important method and thus risking to break the behaviour of the wrapped object.
        
    Examples
    --------
    >>> import numpy as np
    >>>
    >>> arr = np.eye(3)
    >>> wrapper = Wrapper(wrap=arr)
    
    Now the wrapped NumPy array is accessible as `wrapper.wrapped`.
    
    A wrapper class can be used to extend the behaviour:
    
    >>> MyWrapper(Wrapper):
    >>>     wraptype = np.ndarray
    >>>     
    >>>     def invert() -> None:
    >>>         self.wrapped = np.linalg.inv(self.wrapped)
    
    With this solution, you don't have to worry about shadowing an existing
    implementation of NumPy arrays. Not that NumPy arrays might not have a method
    called `invert` at the time of implementing the class `MyWrapper`, but it might
    change in the future. You can even check that internally and get notified: 
    
    >>> import warnings
    >>>
    >>> MyWrapper(Wrapper):
    >>>     wraptype = np.ndarray
    >>>     
    >>>     def invert() -> None:
    >>>         if hasattr(self.wrapped, "invert"):
    >>>             warnings.warn("'invert' already exists in the object")
    >>>         self.wrapped = np.linalg.inv(self.wrapped)
    
    Then, to wrap a NumPy array, you can do this (since the `wraptype` attribute is set,
    the MyWrapper class is going to catch the object to wrap as a positional argument):
    
    >>> wrapper = MyWrapper(arr)
    """
    wrapkey: str = "wrap"
    wraptype: Any = NoneType

    def __init__(self, *args, **kwargs):
        super().__init__()
        self._wrapped = None
        self.wrap(kwargs.get(self.wrapkey, None))

        if self._wrapped is None and self.wraptype is not NoneType:
            for arg in args:
                if isinstance(arg, self.wraptype):
                    self._wrapped = arg
                    break

            if self._wrapped is None:
                try:
                    if self.wraptype is not NoneType:
                        self._wrapped = self.wraptype(*args, **kwargs)
                except Exception:
                    raise ValueError(
                        "Wrapped class '{}' cannot be "
                        + "initiated with these "
                        + "arguments".format(self.wraptype.__name__)
                    )
        else:
            if self.wraptype is not NoneType:
                assert isinstance(
                    self._wrapped, self.wraptype
                ), "Wrong type, unable to wrap object : {}".format(self._wrapped)

    @property
    def wrapped(self):
        """Retruns the wrapped object."""
        return self._wrapped

    def wrap(self, obj: Any=None) -> Any:
        """Wraps the provided object and returns the wrapper instance."""
        if self.wraptype is not NoneType:
            if isinstance(obj, self.wraptype):
                self._wrapped = obj
        else:
            self._wrapped = obj
        return self

    def wraps(self):
        """Returns `True` if the instance wraps something or `False` if it doesn't."""
        return self._wrapped is not None

    def wrapped_obj(self):
        return self._wrapped

    def __hasattr__(self, attr):
        return any([attr in self.__dict__, attr in self._wrapped.__dict__])

    def __getattr__(self, attr):
        if attr in self.__dict__:
            return getattr(self, attr)
        try:
            return getattr(self._wrapped, attr)
        except Exception:
            raise AttributeError(
                "'{}' object has no attribute \
                called {}".format(
                    self.__class__.__name__, attr
                )
            )

    def __getitem__(self, index):
        try:
            return super().__getitem__(index)
        except Exception:
            try:
                return self._wrapped.__getitem__(index)
            except Exception:
                raise TypeError(
                    "'{}' object is not "
                    "subscriptable".format(self.__class__.__name__)
                )

    def __setitem__(self, index, value):
        try:
            return super().__setitem__(index, value)
        except Exception:
            try:
                return self._wrapped.__setitem__(index, value)
            except Exception:
                raise TypeError(
                    "'{}' object does not support "
                    "item assignment".format(self.__class__.__name__)
                )
    
    def __repr__(self) -> str:
        return repr(self._wrapped)
    
    def __str__(self) -> str:
        return str(self._wrapped)


def customwrapper(*, wrapkey:str="wrap", wraptype: Any=NoneType) -> Wrapper:
    """
    A factory function that returns a class decorator turning a class type 
    into a wrapper type, that either
    
    (a) wraps an existing object at object creation provided as a keyword
        argument with wrapkey
    (b) wraps an existing object at object creation if it is a positional
        argument and an instance of wraptype
    (b) wraps the object wraptype(*args, **kwargs)
    
    See also
    --------
    :class:`~sigmaepsilon.core.wrapping.Wrapper`
    
    Examples
    --------
    Take this example from the :class:`~sigmaepsilon.core.wrapping.Wrapper` class:
    
    >>> MyWrapper(Wrapper):
    >>>     wraptype = np.ndarray
    >>>
    >>>     def invert() -> None:
    >>>         self.wrapped = np.linalg.inv(self.wrapped)
    
    An equivalent implementation of this is the following:
    
    >>> @customwrapper(wraptype=np.ndarray)
    >>> MyWrapper:
    >>>     def invert() -> None:
    >>>         self.wrapped = np.linalg.inv(self.wrapped)
    
    Notice how the class `MyWrapper` is not inherited from the `Wrapper` class.
    """

    class BaseWrapperType(Wrapper):
        ...

    BaseWrapperType.wrapkey = wrapkey
    BaseWrapperType.wraptype = wraptype

    def wrapper(BaseType):
        class WrapperType(BaseWrapperType, BaseType):
            basetype = BaseType

        return WrapperType

    return wrapper


def wrapper(BaseType: Any) -> Wrapper:
    """
    Simple class decorator that turns a type into a wrapper with default
    behaviour.
    
    Notes
    -----
    This is the same as using the :func:`~sigmaepsilon.core.wrapping.customwrapper`
    with the default values.
    
    See also
    --------
    :class:`~sigmaepsilon.core.wrapping.Wrapper`
    :func:`~sigmaepsilon.core.wrapping.customwrapper`
    
    Example
    -------
    >>> @wrapper
    >>> MyWrapper:
    >>>     def invert() -> None:
    >>>         self.wrapped = np.linalg.inv(self.wrapped)
    """
    class WrapperType(Wrapper, BaseType):
        basetype = BaseType

    return WrapperType


def wrap(obj: object) -> Wrapper:
    """
    Wraps an object and returns the wrapper.
    
    See also
    --------
    :class:`~sigmaepsilon.core.wrapping.Wrapper`
    
    Example
    -------
    >>> import numpy as np
    >>> wrapper = wrap(np.eye(3))
    """
    return Wrapper(wrap=obj)
