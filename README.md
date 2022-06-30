# Git tooling demo

Using a Python package as an example - this repo is a demo of low-hanging fruit tooling that can improve
your workflow with pre-commit hooks and semantic releases.

## 1. Pre-commit hooks
These are tools configured in [.pre-commit-config.yaml](./.pre-commit-config.yaml), and execute _before_ a commit succeeds.
They enable definition of basic checks to be run as a quality gate before code is checked in (regardless of the branch),
and the commit will only succeed if all of the pre-commit hooks succeed.

Use of pre-commit hooks is on an opt-in basis, even when the configuration is in the repository - each developer must
go through the setup on their local machine for the hooks to be installed, otherwise the hooks won't run on `git commit`.

Installation is simple:
```bash
python3 -m pip install pre-commit && pre-commit install
```

This may take a few minutes to install for the first time, but installation is a one-time thing for each repo.
Note some hooks are wrappers around other executables (e.g. `gitleaks` requires `go` installed), but the bulk
of them rely on Python packages that are automatically pulled down.

## 2. Semantic versioning

This is a versioning scheme which is commonly used, and applies semantics to the version number to communicate patch/minor/major releases.
It pairs up nicely with [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/), whereby structured commit messages communicate the type of
change being made in a commit. There are tools which can parse these structured commit messages to generate a new semantic version and produce a CHANGELOG -
in this repo I'm using [python-semantic-release](https://python-semantic-release.readthedocs.io/en/latest/). Installation and usage is simple:

* Make a change, go for a new commit with some structured commit message e.g. `git commit -m "feat: Trying semantic-release"`
* In a virtual environment run `python3 -m pip install python-semantic-release && semantic-release publish`
  * Note in this repo I'm using `poetry` to manage my virtual environment, so if you have it installed you can also do
    `poetry add -D python-semantic-release && poetry run semantic-release publish`
* This bumps the `__version__` variable in the package source code, the `version` in the metadata (see `pyproject.toml`), updates the CHANGELOG, creates a new Git tag, and can also build/publish the Python package to a Github release and to an atrefact repo.
