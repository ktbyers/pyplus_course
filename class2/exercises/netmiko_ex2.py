from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

password = getpass()

nxos2 = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
    "global_delay_factor": 2,
}

net_connect = ConnectHandler(**nxos2)

cmd = "show lldp neighbors detail"
start_time = datetime.now()
output = net_connect.send_command(cmd)
end_time = datetime.now()
print("#" * 80)
print(output)
print("#" * 80)
print("\n\nExecution Time: {}".format(end_time - start_time))
print()

cmd = "show lldp neighbors detail"
start_time = datetime.now()
output = net_connect.send_command(cmd, delay_factor=8)
net_connect.disconnect()
end_time = datetime.now()
print("#" * 80)
print(output)
print("#" * 80)
print("\n\nExecution Time: {}".format(end_time - start_time))
print()
