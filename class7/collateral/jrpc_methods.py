import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from getpass import getpass
from pprint import pprint
from nxapi_plumbing import Device

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

cmds = ["show hostname", "show version", "show lldp neighbors"]
output = device.show_list(cmds)
print(output)

cmds = ["show version"]
output = device.show_list(cmds, raw_text=True)
pprint(output)

cfg_cmd = ["logging monitor 2"]
output = device.config_list(cfg_cmd)
print(output)

output = device.save()
print(output)

# output = device.checkpoint(filename="my_checkpoint")
