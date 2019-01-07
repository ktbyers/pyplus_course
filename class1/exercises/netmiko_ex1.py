from netmiko import ConnectHandler
from getpass import getpass

nxos1 = {
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_nxos",
}

net_connect = ConnectHandler(**nxos1)
print(net_connect.find_prompt())
