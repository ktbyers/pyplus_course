import pyeapi
from getpass import getpass

password = getpass()
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
print("-" * 12)
arp_list = output[0]['result']['ipV4Neighbors']
for arp_entry in arp_list:
    mac_address = arp_entry['hwAddress']
    ip_address = arp_entry['address']
    print(f"{ip_address} --> {mac_address}")

print("-" * 12)
print()
