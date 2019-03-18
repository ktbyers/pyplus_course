from jnpr.junos import Device
from jnpr.junos.op.ethport import EthPortTable
from getpass import getpass
from pprint import pprint

# import ipdb

a_device = Device(host="srx2.lasthop.io", user="pyclass", password=getpass())
a_device.open()

# ipdb.set_trace()
ports = EthPortTable(a_device)
ports.get()

print(ports)
print(ports.keys())
pprint(ports.values())
pprint(ports.items())
