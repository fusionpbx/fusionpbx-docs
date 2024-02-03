# Configuration file for Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = 'FusionPBX'
author = 'Multiple Authors'

# -- General configuration ---------------------------------------------------

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

html_theme = 'alabaster'
html_static_path = ['source']
