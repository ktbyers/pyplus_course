from pathlib import Path
import pytest
from helpers import subprocess_runner

TEST_CASES = [
    "../class5/exercises/ex1_nxos_bgp.py",
    "../class5/exercises/ex2a_nxos_intf.py",
    "../class5/exercises/ex2b_nxos_bgp.py",
    "../class5/exercises/ex2c_nxos_intf_configure.py",
    "../class5/exercises/ex3_vrf.py",
    "../class5/exercises/ex4_vrf_for_loop.py",
    "../class5/exercises/ex5_full_cfg.py",
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
