# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# For ideas:

# https://github.com/pradyunsg/furo/blob/main/docs/conf.py
# https://github.com/sphinx-gallery/sphinx-gallery/blob/master/doc/conf.py

# --------------------------------------------------------------------------

import sys
import os
from datetime import date

import sigmaepsilon.core as library

from sphinx.config import Config

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("../../src"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = library.__pkg_name__
copyright = "2014-%s, Bence Balogh" % date.today().year
author = "Bence Balogh"


def setup(app: Config):
    app.add_config_value("project_name", project, "html")


# The short X.Y version.
version = library.__version__
# The full version, including alpha/beta/rc tags.
release = "v" + library.__version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # allows to work with markdown files
    "myst_parser",  # pip install myst-parser for this
    # to plot summary about durations of file generations
    "sphinx.ext.duration",
    # to test code snippets in docstrings
    "sphinx.ext.doctest",
    # for automatic exploration of the source files
    "sphinx.ext.autodoc",
    # to enable cross referencing other documents on the internet
    "sphinx.ext.intersphinx",
    # Napoleon is a extension that enables Sphinx to parse both NumPy and Google style docstrings
    "sphinx.ext.napoleon",
    #'sphinx_gallery.gen_gallery',
    #'sphinx_gallery.load_style',  # load CSS for gallery (needs SG >= 0.6)
    #"nbsphinx",  # to handle jupyter notebooks
    #"nbsphinx_link",  # for including notebook files from outside the sphinx source root
    "sphinx_copybutton",  # for "copy to clipboard" buttons
    "sphinx.ext.mathjax",  # for math equations
    #"sphinxcontrib.bibtex",  # for bibliographic references
    #"sphinxcontrib.rsvgconverter",  # for SVG->PDF conversion in LaTeX output
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.extlinks",
    "sphinx.ext.mathjax",
    "sphinx_design",
    "sphinx_inline_tabs",
]

autosummary_generate = True

templates_path = ["_templates"]

exclude_patterns = ["_build"]

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}

# The master toctree document.
master_doc = "index"

language = "EN"

# See warnings about bad links
nitpicky = True
nitpick_ignore = [
    ("", "Pygments lexer name 'ipython' is not known"),
    ("", "Pygments lexer name 'ipython3' is not known"),
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"
pygments_dark_style = "github-dark"
highlight_language = "python3"

intersphinx_mapping = {
    "python": (r"https://docs.python.org/{.major}".format(sys.version_info), None),
    "numpy": (r"https://numpy.org/doc/stable/", None),
    "sphinx": (r"https://www.sphinx-doc.org/en/master", None),
}

# -- MathJax Configuration -------------------------------------------------

mathjax3_config = {
    "tex": {"tags": "ams", "useLabelIds": True},
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"

html_static_path = ["_static"]
