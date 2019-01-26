from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('./templates/exercise2')

#my_vars = {"bgp_as": 22, "router_id": "1.1.1.1", "peer1": "10.20.30.1"}
my_vars = {
    "local_as": 22,
}

template_file = "nxos_bgp.j2"
template = env.get_template(template_file)
output = template.render(**my_vars)
print(output)
