import os
import pyeapi
from getpass import getpass

# import ipdb

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

# ipdb.set_trace()
connection = pyeapi.client.connect(
    transport="https",
    host="arista8.lasthop.io",
    username="pyclass",
    password=password,
    port="443",
)

# enable = getpass("Enable: ")
# device = pyeapi.client.Node(connection, enablepwd=enable)
device = pyeapi.client.Node(connection)
