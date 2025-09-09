import os
from netmiko import ConnectHandler
from getpass import getpass

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()
nxos2 = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
}

net_connect = ConnectHandler(**nxos2)

cmd = "show lldp neighbors detail"
output = net_connect.send_command(cmd)
print()
print("#" * 80)
print(output)
print("#" * 80)
print()

net_connect.disconnect()
