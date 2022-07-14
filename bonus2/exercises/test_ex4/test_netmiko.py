import os
from getpass import getpass
from netmiko import ConnectHandler


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


def test_prompt():
    """Simple test to test netmiko "find_prompt"""
    conn = netmiko_connect()
    assert conn.find_prompt() == "arista1#"


def test_show_version():
    """Simple test to test netmiko "show_version"""
    conn = netmiko_connect()
    assert "4.28.0F" in conn.send_command("show version")
