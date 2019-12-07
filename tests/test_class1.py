from pathlib import Path
import pytest
from helpers import subprocess_runner

TEST_CASES_STDIN = [
    #    ("../day1/strings/solutions/exercise1.py", "Han Solo"),
    #    ("../day1/strings/solutions/exercise2.py", "172.16.21.10"),
    #    ("../day1/numbers/solutions/exercise1.py", "20\n8"),
    #    ("../day1/lists/solutions/exercise2.py", "172.16.21.10"),
]

TEST_CASES = [
    "../class1/exercises/netmiko_ex1.py",
    "../class1/exercises/netmiko_ex2.py",
    "../class1/exercises/netmiko_ex3.py",
    "../class1/collateral/test_connect.py",
    "../class1/collateral/test_dict.py",
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


# @pytest.mark.parametrize("test_case,stdin_response", TEST_CASES_STDIN)
# def test_runner_stdin(test_case, stdin_response):
#     path_obj = Path(test_case)
#     python_script = path_obj.name
#     script_dir = path_obj.parents[0]
#     cmd_list = ["python", python_script]
#     std_out, std_err, return_code = subprocess_runner_stdin(
#         cmd_list, stdin_response, script_dir
#     )
#     assert return_code == 0
#     assert std_err == ""
