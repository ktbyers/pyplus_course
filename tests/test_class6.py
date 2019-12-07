from pathlib import Path
import pytest
from helpers import subprocess_runner


TEST_CASES = [
    "../class6/exercises/ex1_show_ip_arp.py",
    "../class6/exercises/ex2a_yaml_inventory.py",
    "../class6/exercises/ex2b_reusable_func.py",
    "../class6/exercises/ex3_show_routes.py",
    "../class6/exercises/ex4_config_loopbacks.py",
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
