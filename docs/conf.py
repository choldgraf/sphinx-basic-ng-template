# Configuration file for the Sphinx documentation builder.
#
# Full list of options can be found in the Sphinx documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

#
# -- Project information -----------------------------------------------------
#

project = "sphinx-basic-ng sample"
copyright = "2021, Pradyun Gedam"
author = "Pradyun Gedam"

#
# -- General configuration ---------------------------------------------------
#

extensions = ["myst_parser"]
exclude_patterns = [".nox"]
root_doc = "index"

#
# -- Options for HTML output -------------------------------------------------
#

html_theme = "basic-ng-template"
html_context = {
    # "theme_announcement": "Site wide announcement!",
}
