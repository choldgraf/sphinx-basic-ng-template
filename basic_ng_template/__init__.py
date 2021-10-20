"""A modern skeleton for Sphinx themes."""

__version__ = "0.0.1"

from pathlib import Path
from typing import Any, Dict
from functools import lru_cache
import hashlib

import sphinx

_THEME_PATH = (Path(__file__).parent / "theme" / "basic_ng_template").resolve()
_STATIC_PATH = _THEME_PATH / "static"


def _html_page_context(
    app: sphinx.application.Sphinx,
    pagename: str,
    templatename: str,
    context: Dict[str, Any],
    doctree: Any,
) -> None:

    # Add a variable to the Sphinx context
    context["myfootertext"] = "here's some demo footer text!"


def setup(app: sphinx.application.Sphinx) -> Dict[str, Any]:
    """Entry point for sphinx theming."""
    app.require_sphinx("3.0")
    # This activates the theme so users can use it in their docs
    app.add_html_theme("basic-ng-template", str(_THEME_PATH))
    # This adds a basic function that is called each time an HTML page is generated
    app.connect("html-page-context", _html_page_context)

    # Manually add CSS and JS files here so we can use *hashes*.
    # This allows us to do cache-busting without hard-coding the hash in the filename.
    path_css = _STATIC_PATH / "basic-ng-template.css"
    digest_css = hashlib.sha1(path_css.read_bytes()).hexdigest()
    app.add_css_file(f"{path_css.relative_to(_STATIC_PATH)}?digest={digest_css}")
    
    path_js = _STATIC_PATH / "basic-ng-template.js"
    digest_js = hashlib.sha1(path_js.read_bytes()).hexdigest()    
    app.add_js_file(f"{path_js.relative_to(_STATIC_PATH)}?digest={digest_js}")

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
