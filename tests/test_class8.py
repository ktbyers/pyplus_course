from pathlib import Path
import pytest
from helpers import subprocess_runner

TEST_CASES = [
    "../class8/exercises/ex1_jnpr_facts.py",
    "../class8/exercises/ex2_jnpr_tables.py",
    "../class8/exercises/ex3_jnpr_cfg.py",
    "../class8/exercises/ex4_jnpr_cfg_routes.py",
    "../class8/exercises/ex5_jnpr_rpc.py",
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
