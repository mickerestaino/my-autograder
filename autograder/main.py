import re
import subprocess
import sys

import requests


def check_is_git_repo(repo_url: str) -> tuple[bool, str]:
    result = subprocess.run(
        ["git", "ls-remote", repo_url],
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        return True, "Repository is a valid git repository"
    return False, "URL is not a valid git repository"


def check_main_branch(repo_url: str) -> tuple[bool, str]:
    result = subprocess.run(
        ["git", "ls-remote", "--symref", repo_url, "HEAD"],
        capture_output=True,
        text=True,
    )
    if "refs/heads/main" in result.stdout:
        return True, "Main branch is named 'main'"
    return False, "Main branch is not named 'main' (may be 'master' or other)"


def check_feature_branch(repo_url: str) -> tuple[bool, str]:
    result = subprocess.run(
        ["git", "ls-remote", "--heads", repo_url, "feature"],
        capture_output=True,
        text=True,
    )
    if result.stdout.strip():
        return True, "Branch 'feature' exists in the remote"
    return False, "Branch 'feature' not found in the remote"


def _github_repo_path(repo_url: str) -> str | None:
    match = re.search(r"github\.com[/:]([^/]+/[^/]+?)(?:\.git)?$", repo_url)
    return match.group(1) if match else None


def check_file1_exists(repo_url: str) -> tuple[bool, str]:
    repo_path = _github_repo_path(repo_url)
    if not repo_path:
        return False, "Cannot check file1.txt: URL is not a recognized GitHub URL"

    api_url = f"https://api.github.com/repos/{repo_path}/contents/file1.txt?ref=main"
    response = requests.get(api_url, headers={"Accept": "application/vnd.github+json"})
    if response.status_code == 200:
        return True, "file1.txt exists on the 'main' branch"
    return False, "file1.txt not found on the 'main' branch"


CHECKS = [
    check_is_git_repo,
    check_main_branch,
    check_feature_branch,
    check_file1_exists,
]


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: autograder <repo-url>")
        sys.exit(1)

    repo_url = sys.argv[1]

    results = []
    for check in CHECKS:
        passed, message = check(repo_url)
        status = "PASS" if passed else "FAIL"
        print(f"[{status}] {message}")
        results.append(passed)

    print()
    overall = "PASS" if all(results) else "FAIL"
    print(f"Overall: [{overall}]")


if __name__ == "__main__":
    main()
