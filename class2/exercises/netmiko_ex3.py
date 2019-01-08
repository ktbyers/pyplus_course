from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

password = getpass()

device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
}

net_connect = ConnectHandler(**device)

print()
cmds = ['show version', 'show lldp neighbors']
for cmd in cmds:
    output = net_connect.send_command(cmd, use_textfsm=True)
    print('#' * 80)
    print(cmd)
    print('#' * 12)
    pprint(output)
    print('#' * 80)
    print()
