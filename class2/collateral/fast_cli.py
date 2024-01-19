from netmiko import ConnectHandler
from pprint import pprint

device = {
    "device_type": "cisco_ios",
    "host": "cisco1.lasthop.io",
    "username": "student1",
    "use_keys": True,
    "key_file": "~/.ssh/student_key",
    "fast_cli": True,
    "disable_sha2_fix": True,
}

net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())

output = net_connect.send_command("show ip arp", use_textfsm=True)
pprint(output)

output = net_connect.send_config_from_file(config_file="my_changes.txt")
print(output)

net_connect.disconnect()
