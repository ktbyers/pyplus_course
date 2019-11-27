import os
import pyeapi
from getpass import getpass

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

arista8 = {
    "transport": "https",
    "host": "arista8.lasthop.io",
    "username": "pyclass",
    "password": password,
    "port": 443,
}

connection = pyeapi.client.connect(**arista8)
device = pyeapi.client.Node(connection)
output = device.enable("show ip arp")

print()
print("-" * 40)
arp_list = output[0]["result"]["ipV4Neighbors"]
for arp_entry in arp_list:
    mac_address = arp_entry["hwAddress"]
    ip_address = arp_entry["address"]
    print("{:^15}{:^5}{:^15}".format(ip_address, "-->", mac_address))

print("-" * 40)
print()
