from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")

my_vars = {"mode": ""}

template_file = "intf_config3.j2"
template = env.get_template(template_file)
output = template.render(**my_vars)
print(output)
