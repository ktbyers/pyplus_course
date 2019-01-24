from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from pprint import pprint

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")

arp_entry = {
    "interface": "mgmt0",
    "ip": "10.0.0.72",
    "mac": "2C:C2:60:36:32:21",
    "age": 140.0,
}

template_vars = {"arp_entry": arp_entry}

template_file = "template1.j2"
template = env.get_template(template_file)
output = template.render(**template_vars)
print(output)
