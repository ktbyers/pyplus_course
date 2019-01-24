from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")

bgp_vars = {
    "bgp_peer1": True,
    "peer_ip": "1.1.1.1",
    #    "bgp_policy": True,
}

template_file = "bgp_config2.j2"
template = env.get_template(template_file)
output = template.render(**bgp_vars)
print(output)
