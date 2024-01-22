#!/usr/bin/env python
import os
from getpass import getpass
from napalm import get_network_driver

# Supress SSL Certificate Warnings
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


# Device definitions
password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()
cisco3 = dict(
    hostname="cisco3.lasthop.io",
    device_type="ios",
    username="pyclass",
    password=password,
    optional_args={},
)
nxos1 = dict(
    hostname="nxos1.lasthop.io",
    device_type="nxos",
    username="pyclass",
    password=password,
    optional_args={"port": 8443},
)
eos1 = dict(
    hostname="arista1.lasthop.io",
    device_type="eos",
    username="pyclass",
    password=password,
)

# Device we are testing
my_device = cisco3

# NAPALM Class Selection/Object Creation
device_type = my_device.pop("device_type")
driver = get_network_driver(device_type)
device = driver(**my_device)

# NAPALM Action
print()
print("\n\n>>>Test device open")
device.open()

print()
# output = device.get_facts()
output = device.get_config()["running"]
# output = device.get_lldp_neighbors()
print(output)
with open("cisco3.txt", "w") as f:
    f.write(output)
print()
