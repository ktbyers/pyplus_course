import os
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

device = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
}

net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())

output = net_connect.send_command("show ip int brief", use_textfsm=True)
pprint(output)

net_connect.disconnect()
