import os
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lxml import etree
from getpass import getpass
from nxapi_plumbing import Device

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()
prompt = False if os.getenv("PYNET_PASSWORD") else True

device = Device(
    api_format="xml",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=password,
    transport="https",
    port=8443,
    verify=False,
    timeout=60,
)

cmds = ["show hostname", "show version", "show lldp neighbors"]
output = device.show_list(cmds)
for entry in output:
    print(etree.tostring(entry).decode())
    if prompt:
        input("Hit enter to continue: ")

cmds = ["show version"]
output = device.show_list(cmds, raw_text=True)
print(etree.tostring(output[0]).decode())

cfg_cmd = ["logging monitor 2"]
output = device.config_list(cfg_cmd)
print(etree.tostring(output[0]).decode())

output = device.save()
print(output)

# output = device.checkpoint(filename="my_checkpoint2")
# print(output)
