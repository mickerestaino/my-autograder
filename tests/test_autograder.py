"""
Tests for the autograder checks.

Each check function returns (passed: bool, message: str).
Tests use a real public repository where network is available,
and can be extended with mocks for offline/CI environments.
"""

import pytest


# ---------------------------------------------------------------------------
# Placeholder — replace with real imports once autograder/ is implemented
# ---------------------------------------------------------------------------
# from autograder.main import (
#     check_is_git_repo,
#     check_main_branch,
#     check_feature_branch,
#     check_file1_exists,
# )


class TestCheckIsGitRepo:
    def test_valid_repo_passes(self):
        pytest.skip("implement after autograder.main is created")

    def test_invalid_url_fails(self):
        pytest.skip("implement after autograder.main is created")


class TestCheckMainBranch:
    def test_main_branch_passes(self):
        pytest.skip("implement after autograder.main is created")

    def test_master_branch_fails(self):
        pytest.skip("implement after autograder.main is created")


class TestCheckFeatureBranch:
    def test_feature_branch_present_passes(self):
        pytest.skip("implement after autograder.main is created")

    def test_missing_feature_branch_fails(self):
        pytest.skip("implement after autograder.main is created")


class TestCheckFile1Exists:
    def test_file1_present_passes(self):
        pytest.skip("implement after autograder.main is created")

    def test_file1_missing_fails(self):
        pytest.skip("implement after autograder.main is created")
