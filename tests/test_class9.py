from pathlib import Path
import pytest
from helpers import subprocess_runner

TEST_CASES = [
    #    COLLATERAL
    "../class9/collateral/napalm_get.py",
    "../class9/collateral/napalm_get_config.py",
    "../class9/collateral/napalm_simple.py",
    "../class9/collateral/test_merge_nxos.py",
    "../class9/collateral/test_replace.py",
    # Exercises
    "../class9/exercises/ex1_napalm_conn.py",
    "../class9/exercises/ex2_napalm_getters.py",
    "../class9/exercises/ex3_napalm_merge.py",
    "../class9/exercises/ex4_napalm_replace.py",
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
