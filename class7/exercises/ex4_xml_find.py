from __future__ import unicode_literals, print_function
from lxml import etree


def read_xml(filename):
    with open(filename) as infile:
        return etree.fromstring(infile.read())


if __name__ == "__main__":
    filename = "show_security_zones.xml"
    show_security_zones = read_xml(filename)

    print("\n\n")
    print("Find tag of the first zones-security element")
    print("-" * 20)
    first_zone = show_security_zones.find("./zones-security")
    print(first_zone.tag)

    print()
    print("Find the tag of all the child elements of the first security-zone")
    print("-" * 20)
    children = first_zone.getchildren()
    for child in children:
        print(child.tag)

    print("\n\n")
    print("Use the find() method to find the first 'zones-security-zonename' element")
    print("-" * 20)
    print(show_security_zones.find(".//zones-security-zonename").text)

    security_zones = show_security_zones.findall(".//zones-security")
    for zone in security_zones:
        print(zone.find("./zones-security-zonename").text)
    print("\n\n")
