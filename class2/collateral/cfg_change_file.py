import os
from netmiko import ConnectHandler
from getpass import getpass

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

device = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
}

net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())

output = net_connect.send_config_from_file(config_file="my_changes.txt")
print(output)

net_connect.disconnect()
