import os
import pytest
from getpass import getpass
from netmiko import ConnectHandler


# Use function as a fixture to simplify tests
@pytest.fixture(scope="module")
def netmiko_connect():
    """Connect to arista1 and return connection object"""
    password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()
    arista1 = {
        "device_type": "arista_eos",
        "host": "arista1.lasthop.io",
        "username": "pyclass",
        "password": password,
    }
    return ConnectHandler(**arista1)


def test_prompt(netmiko_connect):
    """Simple test to test netmiko "find_prompt"""
    assert netmiko_connect.find_prompt() == "arista1#"


def test_show_version(netmiko_connect):
    """Simple test to test netmiko "show_version"""
    assert "4.20.10M" in netmiko_connect.send_command("show version")
