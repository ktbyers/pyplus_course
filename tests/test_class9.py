from pathlib import Path
import pytest
from helpers import subprocess_runner

TEST_CASES = [
    "../class9/exercises/ex1_napalm_conn.py",
    "../class9/exercises/ex2_napalm_getters.py",
    "../class9/exercises/ex3_napalm_merge.py",
    "../class9/exercises/ex4_napalm_replace.py",
    #    COLLATERAL
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
