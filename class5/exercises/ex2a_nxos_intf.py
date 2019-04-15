from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./templates/exercise2")

interface = "Ethernet1/1"
nxos1 = {"interface": interface, "ipv4_address": "10.1.100.1", "ipv4_netmask": "24"}
nxos2 = {"interface": interface, "ipv4_address": "10.1.100.2", "ipv4_netmask": "24"}

for j2_vars in (nxos1, nxos2):
    template_file = "nxos_ipv4_intf.j2"
    template = env.get_template(template_file)
    output = template.render(**j2_vars)
    print(output)
