from pathlib import Path
import pytest
from helpers import subprocess_runner


TEST_CASES = [
    "../bonus2/exercises/fixme_orig.py",
    #    COLLATERAL
]

TEST_CASES_PYLINT = [
    ("pylint", "../bonus2/exercises/fixme_orig.py", 16),
    ("pylint", "../bonus2/exercises/fixme_pylint.py", 0),
    ("pycodestyle", "../bonus2/exercises/fixme_orig.py", 1),
    ("pycodestyle", "../bonus2/exercises/fixme_pep8.py", 0),
    ("pylama", "../bonus2/exercises/fixme_pep8.py", 0),
    ("pycodestyle", "../bonus2/exercises/fixme_black.py", 0),
    ("pylint", "../bonus2/exercises/fixme_black.py", 16),
]


@pytest.mark.parametrize("test_case", TEST_CASES)
def test_runner(test_case):
    path_obj = Path(test_case)
    python_script = path_obj.name
    script_dir = path_obj.parents[0]
    cmd_list = ["python", python_script]
    std_out, std_err, return_code = subprocess_runner(cmd_list, script_dir)
    assert return_code == 0
    assert std_err == ""

@pytest.mark.parametrize("linter,test_case,test_return_code", TEST_CASES_PYLINT)
def test_runner_pylint(linter, test_case, test_return_code):
    path_obj = Path(test_case)
    python_script = path_obj.name
    script_dir = path_obj.parents[0]
    cmd_list = [linter, python_script]
    std_out, std_err, return_code = subprocess_runner(cmd_list, script_dir)
    assert return_code == test_return_code
    assert std_err == ""
