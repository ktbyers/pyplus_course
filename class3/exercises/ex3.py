"""
3. NAPALM on nxos_ssh returns the following data structure from one of its unit tests (the below is JSON data). Read this JSON data in from a file. Extract the interfaces and IPv4 addresses from this data structure (ignore the IPv6 addresses). Return a new data structure where the key is the interface name and the value is a list containing all of the IPv4 addresses bound to that interface.
"""

"""
{'Ethernet2/1': {'ipv4': {'1.1.1.1': {'prefix_length': 24}}},
 'Ethernet2/2': {'ipv4': {'2.2.2.2': {'prefix_length': 27},
   '3.3.3.3': {'prefix_length': 25}}},
 'Ethernet2/3': {'ipv4': {'4.4.4.4': {'prefix_length': 16}},
  'ipv6': {'fe80::2ec2:60ff:fe4f:feb2': {'prefix_length': 64},
   '2001:db8::1': {'prefix_length': 10}}},
 'Ethernet2/4': {'ipv6': {'fe80::2ec2:60ff:fe4f:feb2': {'prefix_length': 64},
   '2001:11:2233::a1': {'prefix_length': 24},
   '2001:cc11:22bb:0:2ec2:60ff:fe4f:feb2': {'prefix_length': 64}}}}
"""

import json

filename = "nxos_interfaces.json"
with open(filename) as f:
    nxos_data = json.load(f)

ipv4_list = []
ipv6_list = []

for intf, ipaddr_dict in nxos_data.items():
    for k, v in ipaddr_dict.items():
        if k == 'ipv4':
            for ip_addr, prefix_dict in v.items():
                prefix_length = prefix_dict['prefix_length']
                ipv4_list.append("{}/{}".format(ip_addr, prefix_length))
        if k == 'ipv6':
            for ip_addr, prefix_dict in v.items():
                prefix_length = prefix_dict['prefix_length']
                ipv6_list.append("{}/{}".format(ip_addr, prefix_length))

print(ipv4_list)
print(ipv6_list)
