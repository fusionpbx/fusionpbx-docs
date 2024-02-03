# Configuration file for Sphinx documentation builder.

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from conf import *


# -- Project information -----------------------------------------------------

project = 'FusionPBX'
author = 'Multiple Authors'

# -- General configuration ---------------------------------------------------
master_doc = 'index'

# Add any Sphinx extension module names here, as strings.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
]

# -- Options for HTML output -------------------------------------------------

#html_theme = 'alabaster'
#html_static_path = ['_source_']
