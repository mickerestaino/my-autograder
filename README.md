# my-autograder

A CLI tool that checks whether a Git repository meets a set of requirements (valid repo, correct branch names, required files).

## Requirements

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

## Setup

```bash
uv sync
```

This creates a `.venv` and installs both runtime and dev dependencies.

## Running the tool

```bash
uv run autograder <repo-url>
```

Example:

```bash
uv run autograder https://github.com/some-user/some-repo
```

The tool runs four checks and prints a `[PASS]` or `[FAIL]` line for each, followed by an overall result:

```
[PASS] Repository is a valid git repository
[PASS] Main branch is named 'main'
[FAIL] Branch 'feature' not found in the remote
[PASS] file1.txt exists on the 'main' branch

Overall: [FAIL]
```

### Checks

| Check | What it verifies |
|---|---|
| `check_is_git_repo` | The URL points to a reachable Git repository |
| `check_main_branch` | The default branch is named `main` |
| `check_feature_branch` | A branch named `feature` exists |
| `check_file1_exists` | `file1.txt` is present on the `main` branch (GitHub repos only) |

## Running the test suite

```bash
uv run pytest
```

The test file is at [tests/test_autograder.py](tests/test_autograder.py). Tests are currently stubbed with `pytest.skip` and are ready to be implemented once each check is wired up.
