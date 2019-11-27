import yaml
from os import path
from netmiko import ConnectHandler


home_dir = path.expanduser("~")
filename = path.join(home_dir, ".netmiko.yml")

with open(filename) as f:
    yaml_out = yaml.safe_load(f)

cisco3 = yaml_out["cisco3"]
net_connect = ConnectHandler(**cisco3)

print()
print(net_connect.find_prompt())
print()
