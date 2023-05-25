# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Calculator'
copyright = '2023, haseebullah_shaikh'
author = 'haseebullah_shaikh'
release = '0.0.1'

import sys
import os

sys.path.insert(0, os.path.abspath('../'))
sys.path.insert(0, os.path.abspath("../src"))
sys.path.insert(0, os.path.abspath("../src/arithmetic"))
sys.path.insert(0, os.path.abspath("../src/common"))

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "rinoh.frontend.sphinx",  # to generate pdf documentation
    "sphinx.ext.doctest",  # `make doctest` is available now
    "sphinx.ext.autodoc",  # for auto documentation
    "sphinx.ext.duration",  # duration report
    "sphinx.ext.autosummary",  # for generating comprehensive API references
    "sphinx.ext.napoleon",  # for support of Google and NumPy styles in docstrings
]

nitpicky = (
    True  # Sphinx will warn you now about all references where the target cannot be found
	)
templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'bizstyle'
html_static_path = ['_static']

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True