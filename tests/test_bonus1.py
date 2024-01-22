from pathlib import Path
import pytest
from helpers import subprocess_runner


TEST_CASES = [
    #    COLLATERAL
    "../bonus1/collateral/request_get.py",
    "../bonus1/collateral/request_get_w_auth.py",
    "../bonus1/collateral/add_device.py",
    "../bonus1/collateral/delete_device.py",
    "../bonus1/collateral/modify_device.py",
    # Exercises
    "../bonus1/exercises/exercise2a.py",
    "../bonus1/exercises/exercise2b.py",
    "../bonus1/exercises/exercise2c.py",
    "../bonus1/exercises/exercise3a.py",
    "../bonus1/exercises/exercise3b.py",
    "../bonus1/exercises/exercise4.py",
    # the next two are a bit tougher as we are supposed to point to the
    # previously created object
    #    "../bonus1/exercises/exercise5.py",
    #    "../bonus1/exercises/exercise6.py",
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
