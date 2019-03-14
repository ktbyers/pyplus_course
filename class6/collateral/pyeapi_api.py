import pyeapi
from getpass import getpass

connection = pyeapi.client.connect(
    transport="https",
    host="arista8.lasthop.io",
    username="pyclass",
    password=getpass(),
    port="443",
)

enable = getpass("Enable: ")
device = pyeapi.client.Node(connection, enablepwd=enable)

vlan_cfg = device.api("vlans")
print(vlan_cfg)

"""
>>> vlan_cfg
<pyeapi.api.vlans.Vlans object at 0x7f3f39eaac88>
>>> vlan_cfg.getall()
{'1': {'vlan_id': '1', 'name': 'default', 'state': 'active', 'trunk_groups': []}}
>>> vlan_cfg.get(1)
{'vlan_id': 1, 'name': 'default', 'state': 'active', 'trunk_groups': []}
>>> help(vlan_cfg.create)

>>> vlan_cfg.create(225)
True
>>> vlan_cfg.create(226)
True
>>> vlan_cfg.create(226)
True
>>> vlan_cfg.create(227)
True
>>> vlan_cfg.set_name(225, "blue")
True
>>> vlan_cfg.set_name(226, "red")
True
>>> vlan_cfg.set_name(227, "orange")
True
>>> vlan_cfg.getall()
{'1': {'vlan_id': '1', 'name': 'default', 'state': 'active', 'trunk_groups': []}, '225':
{'vlan_id': '225', 'name': 'blue', 'state': 'active', 'trunk_groups': []}, '226':
{'vlan_id': '226', 'name': 'red', 'state': 'active', 'trunk_groups': []}, '227':
{'vlan_id': '227', 'name': 'orange', 'state': 'active', 'trunk_groups': []}}
"""
