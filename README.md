# sphinx-basic-ng-template

This is a simple template repository to prototype what it looks like to sub-theme the [sphinx-basic-ng theme](https://sphinx-basic-ng.readthedocs.io/en/latest/).

## Goals of this template

- Utilize a python-only stack
- Show off some nice workflows for SCSS and JS compilation
- Only utilize the workflows that 80% of themes might be interested in
- Be copyable for other theme authors that want to use this as a starting point

## Notable aspects of this template

### SCSS and JS source files

Stored in `src/scss` and `src/js`, respectively.

These are compiled at build time with the [web-compile package](https://github.com/executablebooks/web-compile) to generate CSS and JS assets for our theme. They are then placed in `basic_ng_template/theme/basic_ng_template/static`.

The compiled CSS and JS assets are **not** included in the commit history of the package (they are listed in `.gitignore`). They will exist locally if you make a commit (via `pre-commit`) or run a build via `nox`, but they won't be included with your GitHub repository online.

This allows you to avoid creating clashes in PRs if multiple people modify an SCSS or JS file at the same time.

### Theme asset linking

Handled by the Python script at `basic_ng_template/__init__.py`.
This uses the `app.add_css_file` and `app.add_js_file` method to link the assets used by this theme.

We also generate a **hash** for each asset that we generate from its file contents.
The hash is used along with a `digest=` parameter, which will cause browsers to update to the latest versions of these assets when they are re-built.

### Theme configuration

Is located in `basic_ng_template/theme/basic_ng_template/theme.conf`.
This is left intentionally minimal - it simply declares the `basic-ng` theme as its parent.

### Theme HTML sections

This theme over-rides all of the sections defined by the `basic-ng` theme.
These are all located in `basic_ng_template/theme/basic_ng_template/sections/<section-name>.html`.
See the [sphinx-basic-ng documentation](https://sphinx-basic-ng.readthedocs.io/en/latest/) for more information about how these sections can be over-ridden.

### Theme HTML components

This theme also defines a custom component that is embedded in a section.
This component is located in `basic_ng_template/theme/basic_ng_template/components/mycustomcomponent.html`.

## Demo this theme

To demonstrate how this theme looks, first clone this repository:

```console
$ git clone https://github.com/choldgraf/sphinx-basic-ng-template
```

install `nox`:

```console
$ pip install nox
```

build the theme with `nox`:

```console
$ nox -s docs-live
```

This will install the necessary dependencies, build the sample documentation for this theme, and open a live server in your browser to preview the theme's built HTML.
