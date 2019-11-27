import os
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

start_time = datetime.now()
device = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
    # "fast_cli": True,
}

net_connect = ConnectHandler(**device)
cmds = ["ip name-server 1.1.1.1", "ip name-server 1.0.0.1", "ip domain-lookup"]
output = net_connect.send_config_set(cmds)
print()
print("#" * 80)
print("CFG Change: ")
print(output)
print("#" * 80)
print()

ping_output = net_connect.send_command("ping google.com")
if "!!" in ping_output:
    print("Ping Successful:")
    print("\n\nPing Output: {}\n\n".format(ping_output))
else:
    raise ValueError("\n\nPing Failed: {}\n\n".format(ping_output))
net_connect.disconnect()

end_time = datetime.now()
print("Total Execution Time: {}\n".format(end_time - start_time))
