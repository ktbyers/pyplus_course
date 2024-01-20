from pathlib import Path
import pytest
from helpers import subprocess_runner

TEST_CASES = [
    # COLLATERAL
    "../class5/collateral/jinja_render1.py",
    "../class5/collateral/jinja_file.py",
    "../class5/collateral/jinja_env.py",
    "../class5/collateral/jinja_cond1.py",
    "../class5/collateral/jinja_cond2.py",
    "../class5/collateral/jinja_cond3.py",
    "../class5/collateral/jinja_cond4.py",
    "../class5/collateral/jinja_vars1.py",
    "../class5/collateral/jinja_vars2.py",
    "../class5/collateral/jinja_vars3.py",
    "../class5/collateral/DICTS/j2_loader.py",
    "../class5/collateral/FILTERS/j2_loader.py",
    "../class5/collateral/INCLUDE/j2_loader.py",
    "../class5/collateral/INCLUDE/j2_loader2.py",
    "../class5/collateral/LISTS/j2_loader.py",
    "../class5/collateral/LOOPS/loops1.py",
    "../class5/collateral/LOOPS/loops2.py",
    "../class5/collateral/LOOPS/loops3.py",
    # Exercises
    "../class5/exercises/ex1_nxos_bgp.py",
    "../class5/exercises/ex2a_nxos_intf.py",
    "../class5/exercises/ex2b_nxos_bgp.py",
    "../class5/exercises/ex2c_nxos_intf_configure.py",
    "../class5/exercises/ex3_vrf.py",
    "../class5/exercises/ex4_vrf_for_loop.py",
    "../class5/exercises/ex5_full_cfg.py",
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
