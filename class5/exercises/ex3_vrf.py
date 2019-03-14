from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./templates/exercise3/")

j2_vars = {"vrf_name": "blue", "rd_number": "100:1", "ipv4_af": True, "ipv6_af": True}

print()
template_file = "ios_vrf.j2"
template = env.get_template(template_file)
cfg = template.render(**j2_vars)
print(cfg)
print()
