"""Development automation."""

from pathlib import Path
import tempfile

import nox

PACKAGE_NAME = "basic_ng_template"
nox.options.sessions = ["docs"]

@nox.session(name="docs-live", reuse_venv=True)
def docs_live(session):
    _install_deps(session)

    with tempfile.TemporaryDirectory() as destination:
        session.run(
            "sphinx-autobuild",
            # for sphinx-autobuild
            "--port=0",
            "--watch=basic_ng_template",
            "--watch=src",
            "--open-browser",
            "--pre-build=web-compile",
            # for sphinx
            "-b=dirhtml",
            "-a",
            "docs",
            destination,
            env={"PYTHONPATH": "."},
        )


@nox.session(reuse_venv=True)
def docs(session):
    _install_deps(session)

    session.run("web-compile")
    session.run(
        "sphinx-build",
        "-b=dirhtml",
        "-v",
        "docs",
        "docs/_build/example-docs",
        env={"PYTHONPATH": "."},
    )

def _install_deps(session):
    if (Path(session.bin) / "sphinx-build").exists() and "reinstall" not in session.posargs:
        return
    session.install("-e", ".[docs]")