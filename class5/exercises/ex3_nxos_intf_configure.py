from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

from netmiko import ConnectHandler
from my_devices import nxos1, nxos2

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('./templates/exercise2')

interface = "Ethernet2/1"

nxos1_vars = {
    "interface": interface,
    "ipv4_address": "10.1.100.1",
    "ipv4_netmask": "24",
}

nxos2_vars = {
    "interface": interface,
    "ipv4_address": "10.1.100.2",
    "ipv4_netmask": "24",
}

nxos1["j2_vars"] = nxos1_vars
nxos2["j2_vars"] = nxos2_vars

for device in (nxos1, nxos2):
    j2_vars = device.pop("j2_vars")
    template_file = "nxos_ipv4_intf.j2"
    template = env.get_template(template_file)
    cfg = template.render(**j2_vars)
    cfg_lines = cfg.strip().splitlines()
    print(cfg_lines)

    # Establish Netmiko Connection
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())
    output = net_connect.send_config_set(cfg_lines)
    print(output)

