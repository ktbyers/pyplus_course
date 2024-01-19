from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "cisco1.lasthop.io",
    "username": "student1",
    "use_keys": True,
    "key_file": "~/.ssh/student_key",
    "disable_sha2_fix": True,
}

net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())
net_connect.disconnect()
