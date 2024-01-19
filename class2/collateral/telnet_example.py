import os
from netmiko import ConnectHandler
from getpass import getpass

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

device = {
    "host": "cisco1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios_telnet",
}

net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())
net_connect.disconnect()
