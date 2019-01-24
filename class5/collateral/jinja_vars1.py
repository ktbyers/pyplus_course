from jinja2 import Template

bgp_config = """
router bgp {{ bgp_as }}
 bgp router-id 10.220.88.20
 bgp log-neighbor-changes
 neighbor 10.220.88.38 remote-as 44
"""

example_expr = """
some text with expressions {{ 13 + 3 }}
other expressions {{ 13 * 7 }}
hello
"""

# my_template = bgp_config
my_template = example_expr
j2_template = Template(my_template)
output = j2_template.render()
print(output)
