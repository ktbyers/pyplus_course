# Python2/3 Compatibility
from __future__ import unicode_literals, print_function
from lxml import etree


# Using a context manager read in the XML file
with open("show_security_zones.xml", "r") as infile:
    # Parse string using etree.fromstring
    show_security_zones = etree.fromstring(infile.read())

# Exercise 1a
print("\n\n")
print("Print the XML variable and its type.")
print("-" * 20)
print(show_security_zones)
print(type(show_security_zones))

# Exercise 1b
print("\n\n")
print("Print the XML tree")
print("-" * 20)
print(etree.tostring(show_security_zones).decode())
# Alternate solution
# print(etree.tostring(show_security_zones, encoding="unicode"))

# Exercise 1c
print("\n\n")
print("Print the name (tag) of the root element")
print("-" * 20)
print(show_security_zones.tag)
print()
print("Print the number of direct children of the root")
print("-" * 20)
print(len(show_security_zones))

# Exercise 1d
print("\n\n")
print("Print the child tag using list indices")
print("-" * 20)
print(show_security_zones[0].tag)

print()
print("Print the child tag using getchildren()")
print("-" * 20)
print(show_security_zones.getchildren()[0].tag)

# Exercise 1e
print("\n\n")
print("Create 'trust_zone' variable and print text of the 'name' child tag")
print("-" * 20)
trust_zone = show_security_zones[0]
print(f"Security zone: {trust_zone[0].text}")

# Exercise 1f
print("\n\n")
print("All children of the 'trust_zone'")
print("-" * 20)
for child in trust_zone:
    print(child.tag)
print("\n\n")
