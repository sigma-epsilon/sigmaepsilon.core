# **sigmaepsilon.core** - Common developer utilities for Python projects

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/sigma-epsilon/sigmaepsilon.core/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/sigma-epsilon/sigmaepsilon.core/tree/main)
[![Documentation Status](https://readthedocs.org/projects/sigmaepsiloncore/badge/?version=latest)](https://sigmaepsiloncore.readthedocs.io/en/latest/?badge=latest)
[![Python 3.7-3.10](https://img.shields.io/badge/python-3.7%E2%80%923.10-blue)](https://www.python.org)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI](https://badge.fury.io/py/sigmaepsilon.core.svg)](https://pypi.org/project/sigmaepsilon.core)

The package contains some usefull stuff for general Python development activites that turned out to be highly reusable during developing projects in the SigmaEpsilon namespace.

Some of the most notable contents:

* Metaprogramming
  * A collection of meta and abstract base classes.
  * A `classproperty` decorator.
  * A solution to enforce abstract class properties on a class.
  
* Wrapping
  * An extendible `Wrapper` class and a few factory functions to help you safely wrap objects.

## **Documentation**

The [documentation](https://sigmaepsiloncore.readthedocs.io/en/latest/) is hosted on ReadTheDocs.

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

If you want to run the tests, you can install the package along with the necessary optional dependencies like this

```console
>>> pip install ".[test]"
```

### For developers

For development purposes, it is suggested to install the package in editable mode, with the optional dependencies for both testing, development and documentation

```console
>>> pip install -e ".[test, dev, docs]"
```

## Testing

To run the tests, run the following command in the root of the project:

```console
>>> pytest
```

## **License**

This package is licensed under the MIT license. See the attached LICENSE file for the details.
