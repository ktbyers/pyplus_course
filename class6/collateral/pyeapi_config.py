import pyeapi
from getpass import getpass

connection = pyeapi.client.connect(
    transport="https",
    host="arista8.lasthop.io",
    username="pyclass",
    password=getpass(),
    port="443",
)

cfg = ["vlan 225", "name green", "vlan 226", "name red"]
device = pyeapi.client.Node(connection)
output = device.config(cfg)
print(output)
