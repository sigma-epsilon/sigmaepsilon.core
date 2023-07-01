# **sigmaepsilon.core** - Common developer utilities for Python projects

The package contains some usefull stuff for general Python development activites that turned out to be highly reusable during developing projects in the SigmaEpsilon namespace.

Some of the most notable contents:

* Metaprogramming
  * A collection of meta and abstract base classes.
  * A `classproperty` decorator.
  * A solution to enforce abstract class properties on a class.
  
* Wrapping
  * An extendible `Wrapper` class and a few factory functions to help you safely wrap objects.

* An `InfixOperator` class to create elegant binary operators.

## **Documentation**

The [documentation](https://sigmaepsilon.core.readthedocs.io/en/latest/) is hosted on ReadTheDocs.

## **Installation**

`sigmaepsilon.core` can be installed (either in a virtual enviroment or globally) from PyPI using `pip` on Python >= 3.7:

```console
>>> pip install sigmaepsilon.core
```

or chechkout with the following command using GitHub CLI

```console
gh repo clone sigma-epsilon/sigmaepsilon.core
```

and install from source by typing

```console
>>> pip install .
```

## **License**

This package is licensed under the MIT license.
