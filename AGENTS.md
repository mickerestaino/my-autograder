# AGENTS.md

## Project overview

This is a Python CLI autograder that takes a public GitHub repository URL and reports, **for each condition individually**, whether it is met or not. The conditions are defined in [specs/spec-autograde.md](specs/spec-autograde.md).

### Checks performed

Given a repository URL the tool reports the result of each check independently:

1. The URL points to a valid git repository.
2. The default branch is named `main` (not `master`).
3. A branch named `feature` exists in the remote.
4. A file named `file1.txt` exists on the `main` branch.

---

## Toolchain

| Tool | Purpose |
|------|---------|
| [uv](https://github.com/astral-sh/uv) | Dependency management and virtual environment |
| [pytest](https://docs.pytest.org/) | Test runner |

### Setup

```bash
# Install dependencies and create the virtual environment
uv sync

# Run the CLI
uv run python -m autograder <repo-url>

# Run tests
uv run pytest
```

---

## Project structure

```
my-autograder/
├── AGENTS.md          # This file — project instructions for agents
├── pyproject.toml     # Project metadata, dependencies, entry point
├── specs/
│   └── spec-autograde.md   # Human-readable specification
├── autograder/
│   ├── __init__.py
│   └── main.py        # CLI entry point and grading logic
└── tests/
    ├── __init__.py
    └── test_autograder.py  # pytest test suite
```

---

## Coding conventions

- All logic lives in `autograder/`.
- The CLI is invoked as `python -m autograder <repo-url>`.
- The CLI prints one result line per check (e.g. `[PASS] main branch is named 'main'` or `[FAIL] no 'feature' branch found`).
- Each check is implemented as an independent function that returns `(passed: bool, message: str)`.
- Tests live in `tests/` and use `pytest`. No mocking of the filesystem — use real subprocess or network calls where possible; mock the GitHub API when network access is unavailable.
- Use `uv` exclusively for dependency management; do not use `pip` directly.
- Type-annotate all public functions.
- Keep functions small and focused; avoid side effects outside of `main()`.

---

## Adding a new check

1. Implement a function `check_<name>(repo_url: str) -> tuple[bool, str]` in `autograder/main.py`.
2. Register it in the `CHECKS` list in the same file.
3. Add a corresponding test in `tests/test_autograder.py`.
