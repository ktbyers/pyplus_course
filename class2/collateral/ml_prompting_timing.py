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

# Behavior depends upon the 'file prompt quiet' setting.
# The below assumes 'file prompt quiet' (i.e. that it is configured).
filename = "jd-show_ip_int_brief.txt"
command = f"delete flash:/{filename}"
output = net_connect.send_command_timing(
    command, strip_prompt=False, strip_command=False
)
output += net_connect.send_command_timing("y", strip_prompt=False, strip_command=False)
print(output)
net_connect.disconnect()
