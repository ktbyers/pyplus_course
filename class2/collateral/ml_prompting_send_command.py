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
# The below assumes 'no file prompt quiet' (i.e. that it is not configured).
filename = "filename1.txt"
command = f"delete flash:/{filename}"
output = net_connect.send_command(
    command, expect_string=r"Delete filename", strip_prompt=False, strip_command=False
)
output += net_connect.send_command(
    "\n", expect_string=r"confirm", strip_prompt=False, strip_command=False
)
output += net_connect.send_command(
    "y", expect_string=r"#", strip_prompt=False, strip_command=False
)
print(output)
net_connect.disconnect()
