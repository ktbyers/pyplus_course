import pytest
from getpass import getpass
from netmiko import ConnectHandler

password = getpass()


@pytest.fixture(scope="module")
def netmiko_conn(request):
    net_connect = ConnectHandler(
        host="cisco3.lasthop.io",
        device_type="cisco_ios",
        username="pyclass",
        password=password,
    )

    def fin():
        net_connect.disconnect()

    request.addfinalizer(fin)
    return net_connect


def test_find_prompt(netmiko_conn):
    assert "cisco3#" in netmiko_conn.find_prompt()


def test_send_command(netmiko_conn):
    output = netmiko_conn.send_command("show ip int brief")
    assert "10.220.88.22" in output
