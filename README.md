# cv-generator


## Development

The project uses Poetry for dependency management and `pyproject.toml` for configuration.

To start development it should be enough to simply run

```bash
poetry install --with dev
```

That will install `pylint`, `black` and `pre-commit` - for the time being that hook is treated as this projects dedicated __*"pipeline"*__. If it fails - treat that as a pipeline failing.

If the pre-commit hook is being weird - please try running the tests manually:
```bash
poetry run pylint src
poetry run black src
```

__*TODO*__: Look into GitHub actions.
