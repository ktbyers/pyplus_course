from pathlib import Path
import pytest
from helpers import subprocess_runner


TEST_CASES = [
    "../class3/exercises/data_struct_ex1.py",
    "../class3/exercises/data_struct_ex2.py",
    "../class3/exercises/data_struct_ex3.py",
    "../class3/exercises/data_struct_ex4.py",
    "../class3/exercises/yaml_ex5.py",
    "../class3/exercises/confparse_ex6.py",
    "../class3/exercises/confparse_ex7.py",
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
