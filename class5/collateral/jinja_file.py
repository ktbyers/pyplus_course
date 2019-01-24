from jinja2 import Template

filename = "bgp_config.j2"
with open(filename) as f:
    my_template = f.read()

template_vars = {"bgp_as": 22, "router_id": "1.1.1.1", "peer1": "10.20.30.1"}

j2_template = Template(my_template)
output = j2_template.render(**template_vars)
print(output)
