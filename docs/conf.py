# Configuration file for Sphinx documentation builder.

import sys
import os

sys.path.insert(0, os.path.abspath("../source"))

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

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
