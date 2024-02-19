# **SigmaEpsilon.Core** - Common developer utilities for Python projects

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/sigma-epsilon/sigmaepsilon.core/tree/main.svg?style=shield)](https://dl.circleci.com/status-badge/redirect/gh/sigma-epsilon/sigmaepsilon.core/tree/main)
[![Documentation Status](https://readthedocs.org/projects/sigmaepsiloncore/badge/?version=latest)](https://sigmaepsiloncore.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/sigma-epsilon/sigmaepsilon.core/graph/badge.svg?token=WNLDFIGGL6)](https://codecov.io/gh/sigma-epsilon/sigmaepsilon.core)
[![Python](https://img.shields.io/badge/python-3.10%E2%80%923*-blue)](https://www.python.org)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI](https://badge.fury.io/py/sigmaepsilon.core.svg)](https://pypi.org/project/sigmaepsilon.core)
[![Requirements Status](https://dependency-dash.repo-helper.uk/github/sigma-epsilon/sigmaepsilon.core/badge.svg)](https://dependency-dash.repo-helper.uk/github/sigma-epsilon/sigmaepsilon.core)

The package contains some usefull stuff for general Python development activites that turned out to be highly reusable during developing projects in the SigmaEpsilon namespace.

Some of the most notable contents:

* Metaprogramming
  * A collection of meta and abstract base classes.
  * A `classproperty` decorator.
  * A solution to enforce abstract class properties on a class.
  * Reusable facilities for project configuration, testing, exceptions, etc.
  
* Wrapping
  * An extendible `Wrapper` class and a few factory functions to help you safely wrap objects.

## **Documentation**

The [documentation](https://sigmaepsiloncore.readthedocs.io/en/latest/) is built with [Sphinx](https://www.sphinx-doc.org/en/master/) using the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) and hosted on [ReadTheDocs](https://readthedocs.org/).

## **Installation**

Before attempting to install the package, it is suggested to upgrade pip:

```console
python -m pip install --upgrade pip
```

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

### Development mode

For development purposes, it is suggested to install the package in editable mode, with the optional dependencies for both testing, development and documentation

```console
>>> pip install -e ".[test, dev, docs]"
```

## Testing and coverage

To run the tests, run the following command in the root of the project:

```console
python -m pytest --cov-report html --cov-config=.coveragerc --cov sigmaepsilon.core
```

## **License**

This package is licensed under the [MIT license](https://opensource.org/license/mit/). See the attached LICENSE file for the details.
