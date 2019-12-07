from pathlib import Path
import pytest
from helpers import subprocess_runner


TEST_CASES = [
    "../class10/exercises/ex1_serial.py",
    "../class10/exercises/ex2_legacy_threads.py",
    "../class10/exercises/ex3a_cf_wait.py",
    "../class10/exercises/ex3b_cf_ascompleted.py",
    "../class10/exercises/ex4_cf_ascompleted_procs.py",
    "../class10/exercises/ex5_cf_procs_cm.py",
    "../class10/exercises/ex6_cf_map.py",
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
