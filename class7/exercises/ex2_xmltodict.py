from __future__ import unicode_literals, print_function
from pprint import pprint
import xmltodict


with open("show_security_zones.xml") as infile:
    show_security_zones = xmltodict.parse(infile.read())


print("\n\n")
print("Print the new variable and its type")
print("-" * 20)
pprint(show_security_zones)
print(type(show_security_zones))

print("\n\n")
print("Print out index and name of the security zones")
print("-" * 20)
zones = show_security_zones["zones-information"]["zones-security"]
for index, zone in enumerate(zones):
    print(f"Security Zone #{index + 1}: {zone['zones-security-zonename']}")
print("\n\n")
