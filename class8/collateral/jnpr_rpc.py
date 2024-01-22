#!/usr/bin/env python
import os
from jnpr.junos import Device
from lxml import etree
from getpass import getpass

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

juniper_srx = {"host": "srx2.lasthop.io", "user": "pyclass", "password": password}

a_device = Device(**juniper_srx)
a_device.open()

# show version | display xml rpc
# <get-software-information>
# xml_out = a_device.rpc.get_software_information()
# print(etree.tostring(xml_out, encoding="unicode"))

# get_lldp_neighbors_information()
xml_out = a_device.rpc.get_lldp_neighbors_information()
print(etree.tostring(xml_out, encoding="unicode"))
