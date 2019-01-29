from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")

base_intf = "GigabitEthernet0/1/"
intf_list = []
for intf_number in range(24):
    intf_name = f"{base_intf}{intf_number}"
    intf_list.append(intf_name)

intf_vars = {"intf_list": intf_list}

template_file = "template1.j2"
template = env.get_template(template_file)
output = template.render(**intf_vars)
print(output)
