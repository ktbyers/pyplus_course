import pyeapi
from getpass import getpass

connection = pyeapi.client.connect(
    transport="https",
    host="arista8.lasthop.io",
    username="pyclass",
    password=getpass(),
    port="443",
)

# enable = getpass("Enable: ")
# device = pyeapi.client.Node(connection, enablepwd=enable)
device = pyeapi.client.Node(connection)
output = device.enable(["show version", "show ip arp"])
print(output)
