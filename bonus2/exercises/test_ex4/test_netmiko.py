from getpass import getpass
from netmiko import ConnectHandler


def netmiko_connect():
    """Connect to arista1 and return connection object"""
    arista1 = {
        "device_type": "arista_eos",
        "host": "arista1.lasthop.io",
        "username": "pyclass",
        "password": getpass(),
    }
    return ConnectHandler(**arista1)


def test_prompt():
    """Simple test to test netmiko "find_prompt"""
    conn = netmiko_connect()
    assert conn.find_prompt() == "arista1#"


def test_show_version():
    """Simple test to test netmiko "show_version"""
    conn = netmiko_connect()
    assert "4.20.10M" in conn.send_command("show version")
