import os
import pyeapi
from getpass import getpass

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

connection = pyeapi.client.connect(
    transport="https",
    host="arista8.lasthop.io",
    username="pyclass",
    password=password,
    port="443",
)

cfg = ["vlan 225", "name green", "vlan 226", "name red"]
device = pyeapi.client.Node(connection)
output = device.config(cfg)
print(output)
