from __future__ import unicode_literals, print_function
import os
from getpass import getpass
from lxml import etree
from nxapi_plumbing import Device

# Disable Self-signed Certificate Warnings
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()
# Create nxapi_plumbing Device object
device = Device(
    api_format="xml",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=password,
    transport="https",
    port=8443,
    verify=False,
)

# Exercise 7a
print("\n\n")
print("Gather and print Ethernet1/1 Data")
print("-" * 20)
intf_output = device.show("show interface Ethernet1/1")
print(
    "Interface: {}; State: {}; MTU: {}".format(
        intf_output.find(".//interface").text,
        intf_output.find(".//state").text,
        intf_output.find(".//eth_mtu").text,
    )
)

# Exercise 7b
print("\n\n")
print("Capture and print XML output from multiple show commands")
print("-" * 20)
show_output = device.show_list(["show system uptime", "show system resources"])
for output in show_output:
    print(etree.tostring(output, encoding="unicode"))
    print("-" * 20)
print("\n\n")

# Exercise 7c
print()
print("Create two new loopbacks with descriptions")
print("-" * 20)
commands = [
    "interface loopback101",
    "description loopback101",
    "no shutdown",
    "interface loopback102",
    "description loopback102",
    "no shutdown",
]
output = device.config_list(commands)
# Look at the output XML for each configuration command
for msg in output:
    print(etree.tostring(msg, encoding="unicode"))
