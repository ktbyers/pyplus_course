from __future__ import unicode_literals, print_function
from pprint import pprint
import xmltodict


# Using a context manager; open file in 'read' mode
with open("show_security_zones.xml", "r") as infile:
    show_security_zones = xmltodict.parse(infile.read())


print("\n\n")
print("Print the new variable and its type")
print("-" * 20)
pprint(show_security_zones)
print(type(show_security_zones))

# Print out the number and name of all the security zones
print("\n\n")
print("Print out index and name of security zones")
print("-" * 20)
zones = show_security_zones["security"]["zones"]["security-zone"]
for index, zone in enumerate(zones):
    print(f"Security Zone #{index + 1}: {zone['name']}")

import ipdb
ipdb.set_trace()

# Remove the 'untrust' security zone fromo the dictionary
print()
print("Remove 'untrust' security zone from dictionary")
print("-" * 20)
zones = show_security_zones["security"]["zones"]["security-zone"]
show_security_zones["security"]["zones"]["security-zone"].pop(1)

# Convert the dictionary back to an XML file
print()
print("'Unparse' the dictionary back to an XML file")
print("-" * 20)
with open("show_security_zones_single_zone.xml", "w") as outfile:
    outfile.write(xmltodict.unparse(show_security_zones, pretty=True))
