Create a public repository on GitHub named "my-autograde". The Python CLI tool needs to take as input a valid repository URL and return for each one of the conditions if they are met or not.

1. The repository should be a git repository.
2. The main branch should be called `main` and not `master`
3. There is a `feature` branch in the remote repository.
4. A file named `file1.txt` exists on the `main` branch of the repository.

After reporting each individual check, the tool must print an overall result: `[PASS]` if all checks pass, or `[FAIL]` if at least one check fails.