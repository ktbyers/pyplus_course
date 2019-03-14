from __future__ import unicode_literals, print_function
from getpass import getpass
from nxapi_plumbing import Device

# Disable Self-signed Certificate Warnings
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


device = Device(
    api_format="jsonrpc",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=getpass(),
    transport="https",
    port=8443,
    verify=False,
)

print("\n\n")
print("Gather and print Ethernet2/1 data:")
print("-" * 20)
intf_output = device.show("show interface Ethernet2/1")
intf_output = intf_output["TABLE_interface"]["ROW_interface"]
print("Interface: {interface}; State: {state}; MTU: {eth_mtu}".format(**intf_output))
print("\n\n")
