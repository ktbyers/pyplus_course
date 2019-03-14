from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./templates/exercise4")

my_vrfs = [
    {"vrf_name": "blue1", "rd_number": "100:1", "ipv4_af": True, "ipv6_af": True},
    {"vrf_name": "blue2", "rd_number": "100:2", "ipv4_af": True, "ipv6_af": True},
    {"vrf_name": "blue3", "rd_number": "100:3", "ipv4_af": True, "ipv6_af": True},
    {"vrf_name": "blue4", "rd_number": "100:4", "ipv4_af": True, "ipv6_af": True},
    {"vrf_name": "blue5", "rd_number": "100:5", "ipv4_af": True, "ipv6_af": True},
]

j2_vars = {"my_vrfs": my_vrfs}

template_file = "ios_vrf.j2"
template = env.get_template(template_file)
cfg = template.render(**j2_vars)
print(cfg)
