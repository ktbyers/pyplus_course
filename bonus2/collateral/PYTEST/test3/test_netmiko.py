from getpass import getpass
from netmiko import ConnectHandler


def netmiko_conn():
    net_connect = ConnectHandler(
        host="cisco3.lasthop.io",
        device_type="cisco_ios",
        username="pyclass",
        password=getpass(),
    )
    return net_connect


def test_find_prompt():
    net_connect = netmiko_conn()
    assert "cisco3#" in net_connect.find_prompt()


def test_send_command():
    net_connect = netmiko_conn()
    output = net_connect.send_command("show ip int brief")
    assert "10.220.88.22" in output
