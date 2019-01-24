from jinja2 import Template

bgp_config = """
router bgp {{ bgp_as }}
 bgp router-id {{ router_id }}
 bgp log-neighbor-changes
 neighbor {{ peer1 }} remote-as 44
"""

my_vars = {"bgp_as": 22, "router_id": "1.1.1.1", "peer1": "10.20.30.1"}

j2_template = Template(bgp_config)
output = j2_template.render(**my_vars)
print(output)
