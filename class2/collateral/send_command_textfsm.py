from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

device1 = {
    "host": "cisco1.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_ios_telnet",
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

output = net_connect.send_command("show ip int brief", use_textfsm=True)
pprint(output)

net_connect.disconnect()
