from pathlib import Path
import pytest
from helpers import subprocess_runner


TEST_CASES = [
    # COLLATERAL
    "../class6/collateral/eapi_simple.py",
    "../class6/collateral/eapi_config.py",
    "../class6/collateral/pyeapi_simple.py",
    "../class6/collateral/pyeapi_show.py",
    "../class6/collateral/pyeapi_config.py",
    # "../class6/collateral/pyeapi_w_conf.py",
    "../class6/collateral/pyeapi_api.py",
    # Exercises
    "../class6/exercises/ex1_show_ip_arp.py",
    "../class6/exercises/ex2a_yaml_inventory.py",
    "../class6/exercises/ex2b_reusable_func.py",
    "../class6/exercises/ex3_show_routes.py",
    "../class6/exercises/ex4_config_loopbacks.py",
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
