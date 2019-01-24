from jinja2 import Template

text1 = """
this is some template
that has multiple lines
of text in it

"""

bgp_config = """
router bgp 42
 bgp router-id 10.220.88.20
 bgp log-neighbor-changes
 neighbor 10.220.88.38 remote-as 44
"""

j2_template = Template(bgp_config)
output = j2_template.render()
print(output)
