# Development of hntpy

## Poetry for package management

This project uses [poetry](https://python-poetry.org/) for dependency management, general package management, and publishing to PyPI.

For a helpful guide on instructions for how to use poetry for package management with PyPI, read this [blog](https://johnfraney.ca/blog/create-publish-python-package-poetry/).

The main commands used are summarized in the sections below. All commands should be run from the root `htnpy/` directory (where the `pyproject.toml` file is).

## Dependency management

To add a new python dependency to the project:

```bash
poetry add loguru
```

To remove a dependency, run:

```bash
poetry remove loguru
```

**Note**: pass the `--dev` flag to add or remove the dependency as a dev only package.

## Testing with pytest

To run tests, simply run:

```bash
poetry run pytest
```

To run tests and output test coverage, run:

```bash
poetry run pytest --cov hntpy/
```

To get test coverage and line #'s that are missing test coverage per file:

```bash
poetry run pytest --cov-report term-missing --cov hntpy
```

## Publishing to PyPI

First, change the version number the `pyproject.toml`. You can't republish over an existing version on PyPI, so you need to increment this version number each time you publish.

After that, run:

```bash
poetry build
```

This builds a new version of the package, and saves the build in the `dist/` folder.

Then, run the following to pubish to PyPI:

```bash
poetry publish
```

## Documentation

To add more badges/shields in readme's, visit [https://shields.io/](https://shields.io/).
