from pathlib import Path
import pytest
from helpers import subprocess_runner

TEST_CASES = [
    "../class2/collateral/delay_factor.py",
    "../class2/collateral/global_delay.py",
    "../class2/collateral/ssh_keys.py",
    "../class2/collateral/telnet_example.py",
    "../class2/collateral/send_command_textfsm.py",
    "../class2/collateral/nm_file_transfer.py",
    "../class2/collateral/cfg_change.py",
    "../class2/collateral/cfg_change_file.py",
    "../class2/collateral/cfg_change_save.py",
    "../class2/collateral/fast_cli.py",
    "../class2/exercises/netmiko_ex1a.py",
    "../class2/exercises/netmiko_ex1b.py",
    "../class2/exercises/netmiko_ex2.py",
    "../class2/exercises/netmiko_ex3.py",
    "../class2/exercises/netmiko_ex4.py",
    "../class2/exercises/netmiko_ex5.py",
    "../class2/exercises/netmiko_ex6.py",
    # Can't test easily as you need to know the filename in flash
    #    "../class2/collateral/ml_prompting_send_command.py",
    #    "../class2/collateral/ml_prompting_timing.py",
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
