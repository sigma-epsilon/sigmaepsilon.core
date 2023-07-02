# -*- coding: utf-8 -*-
from .meta import *


__all__ = ["ABC_Strong", "ABC_Weak", "ABC_Safe"]


class ABC_Weak(metaclass=ABCMeta_Weak):
    """
    Helper class that provides a standard way to create an ABC using
    inheritance. It follows weak abstraction in the meaning, that
    it is enough to implement the abstarcts in the instance, they impose no
    restriction on the inherited class itself. Therefore, error only occurs at
    runtime.
    
    Notes
    -----
    This class provides nothing over the default behaviour offered by Python's
    standard library, but it is equipped with some useful machinery for
    subclasses that do. All other metaclasses of this module are subclasses of this
    class.
    
    See also
    --------
    :class:`~sigmaepsilon.core.meta.ABCMeta_Weak`

    Examples
    --------
    Create an abstract class with an abstract instance method.

    >>> class ABC_Parent_Weak(ABC_Weak):
    >>>     @abstractmethod
    >>>     def abc_method_parent(self):
    >>>         pass

    Now if we subclass our parent class without implementing `abc_method_parent`,
    nothing happens at runtime (when the class is created).

    >>> class ABC_Child_Weak(ABC_Parent_Weak):
    >>>     @abstractmethod
    >>>     def abc_method_child(self):
    >>>         pass

    If we create an instance with implementing the abstract classes prescribed,
    it works fine.

    >>> class MyClass(ABC_Parent_Weak):
    >>>     def abc_method_child(self):
    >>>         pass
    ...
    >>>     def abc_method_parent(self):
    >>>         pass
    ...
    >>> foo = MyClass()

    If miss any of the required implementations, we can see a `TypeError`:

    >>> class MyClass(ABC_Parent_Weak):
    >>>     def abc_method_child(self):
    >>>         pass
    ...
    >>> foo = MyClass()
    Traceback (most recent call last):
        ...
    TypeError: Can't instantiate abstract class MyClass with abstract methods abc_method_parent
    """
    __slots__ = ()


class ABC_Strong(metaclass=ABCMeta_Strong):
    """
    Helper class that provides a standard way to create an ABC using
    inheritance. It follows strong abstraction in the meaning, that
    an abstract function of any of the base classes must be implemented or
    delayed with the use of another @abstractmethod decorator.
    Contrary to the weak metaclass, error occurs when the class is created.
    
    See also
    --------
    :class:`~sigmaepsilon.core.meta.ABCMeta_Strong`

    Examples
    --------
    Create an abstract class with abstract instance methods.

    >>> class MyParentAbstractClass(ABC_Strong):
    >>>     @abstractmethod
    >>>     def my_abstract_method_A(self):
    >>>         pass
    ...
    >>>     @abstractmethod
    >>>     def my_abstract_method_B(self):
    >>>         pass

    Now if we subclass our parent class, we can either provide an implementation
    of our abstract methods, or delay the implementation by using the `abstractmethod`
    decorator again.

    >>> class MyChildAbstractClass(MyParentAbstractClass):
    >>>     @abstractmethod
    >>>     def my_abstract_method_A(self):
    >>>         # this is delayed
    >>>         pass
    ...
    >>>     def my_abstract_method_B(self):
    >>>         pass

    In every other case, we will se an error when the class is created.

    >>> class MyChildAbstractClass(MyParentAbstractClass):
    >>>     @abstractmethod
    >>>     def my_abstract_method_A(self):
    >>>         pass
    Traceback (most recent call last):
        ...
    TypeError: Can't create abstract class MyChildAbstractClas! MyChildAbstractClas must implement abstract method my_abstract_method_B of class MyParentAbstractClass.
    """
    __slots__ = ()


class ABC_Safe(metaclass=ABCMeta_Safe):
    """
    Helper class that provides a standard way to create an ABC using
    inheritance. Throws a `TypeError`
    if a method tries to shadow a method in any of the base
    classes.
    
    See also
    --------
    :class:`~sigmaepsilon.core.meta.ABCMeta_Safe`

    Examples
    --------
    Create an abstract class with an instance method.

    >>> class ABC_Parent_Safe(ABC_Safe):
    >>>     def funcParentSafe(self):
    >>>         pass

    Now, if we try to overload any implementation in the parent class, we
    got a `TypeError` when the class is created.

    >>> class ABC_Child_Safe(ABC_Parent_Safe):
    >>>     def funcParentSafe(self):
    >>>         pass
    Traceback (most recent call last):
        ...
    TypeError: Can't create abstract class ABC_Child_Safe! Method funcParentSafe is already implemented in class ABC_Parent_Safe.
    """
    __slots__ = ()

