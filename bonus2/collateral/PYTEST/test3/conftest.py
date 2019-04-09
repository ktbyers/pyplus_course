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
