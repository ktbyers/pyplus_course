import os
from jnpr.junos import Device
from jnpr.junos.op.ethport import EthPortTable
from getpass import getpass
from pprint import pprint

# import ipdb
password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

a_device = Device(host="srx2.lasthop.io", user="pyclass", password=password)
a_device.open()

# ipdb.set_trace()
ports = EthPortTable(a_device)
ports.get()

print(ports)
print(ports.keys())
pprint(ports.values())
pprint(ports.items())
