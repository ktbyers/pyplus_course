# Python2/3 Compatibility
from __future__ import unicode_literals, print_function
# Import etree to handle our xml file
from lxml import etree


# Using a context manager; open file in 'read' mode
with open("show_security_zones.xml", "r") as infile:
    # Use etree.fromstring to read in the file
    show_security_zones = etree.fromstring(infile.read())

# Printing out the newly created variable
print()
print("Print the new variable and type of the new variable")
print("-" * 20)
print(show_security_zones)
print(type(show_security_zones))

# Print out the entirety of the XML file -- make sure to set "pretty_print" to
# True. Is the output "pretty"? Why not? Print it again, but ensuring that the
# otuput is "pretty".
print()
print("Print the XML object")
print("-" * 20)
print(etree.tostring(show_security_zones, pretty_print=True))

# Two methods to decode to "pretty" the output:
print()
print("Print the 'pretty' XML object method 1")
print("-" * 20)
print(etree.tostring(show_security_zones, pretty_print=True).decode())
print()
print("Print the 'pretty' XML object method 2")
print("-" * 20)
print(etree.tostring(show_security_zones, pretty_print=True,
                     encoding="unicode"))

# Before attempting to access child elements, print out the value of the tag
# at the root of the tree -- this should be the "security" tag
print()
print("Print the top level name tag at the root of XML object")
print("-" * 20)
print(show_security_zones.tag)

# Determine the quantity of child elements of the "security" tag; this will
# help us understand the trees structure so that we can properly traverse it
print()
print("Print the length of the root XML object")
print("-" * 20)
print(len(show_security_zones))

# Access the child element via list indicies; print the tag method 1
print()
print("Print the child element and child element name tag method 1")
print("-" * 20)
print(show_security_zones[0])
print(show_security_zones[0].tag)

# Access the child element via getchildren; print the tag method 2
print()
print("Print the child element and child element name tag method 2")
print("-" * 20)
print(show_security_zones.getchildren()[0])
print(show_security_zones.getchildren()[0].tag)

# Create 'trust_zone' variable; access text of 'name' child tag
print()
print("Create 'trust_zone' variable and print text of the name child tag")
print("-" * 20)
trust_zone = show_security_zones[0][0]
print(trust_zone[0].text)

# Iterate through all children of 'trust_zone' print tags of children
print()
print("Iterate through all children of 'trust_zone', print tags of children")
print("-" * 20)
for child in trust_zone:
    print(child.tag)

# Print the tag "security" as that is the root of all of the elements we've
# been working with in this exercise
print()
print("Print the tag for root of the previous child element")
print("-" * 20)
print(child.getroottree().getroot().tag)
