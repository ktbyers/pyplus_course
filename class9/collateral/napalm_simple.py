#!/usr/bin/env python
import os
from getpass import getpass
from pprint import pprint
from napalm import get_network_driver

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

cisco3 = dict(
    hostname="cisco3.lasthop.io",
    device_type="ios",
    username="pyclass",
    password=password,
    optional_args={},
)

device_type = cisco3.pop("device_type")
driver = get_network_driver(device_type)
device = driver(**cisco3)

print()
print("\n\n>>>Test device open")
device.open()

print()
output = device.get_facts()
pprint(output)
print()
