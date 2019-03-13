from __future__ import unicode_literals, print_function
import xmltodict


def read_xml(filename, force_list=False):
    with open(filename, "r") as infile:
        return xmltodict.parse(infile.read(), force_list=force_list)


if __name__ == "__main__":

    filename = "show_security_zones.xml"
    show_security_zones = read_xml(filename)

    filename = "show_security_zones_trust.xml"
    show_security_zones_single = read_xml(filename)

    # Print out the type of the element 'security-zone' in original XML document
    print("Type of 'security-zone' in original XML file")
    print("-" * 20)
    print(type(show_security_zones['zones-information']['zones-security']))

    # Print out the type of the element 'security-zone' in updated XML document
    print()
    print("Type of 'security-zone' in modified XML file with only one zone")
    print("-" * 20)
    print(type(show_security_zones_single['zones-information']['zones-security']))

    filename = "show_security_zones_trust.xml"
    show_security_zones_single = read_xml(filename, force_list=True)
    print(type(show_security_zones_single['zones-information']['zones-security']))


## Using a context manager; open file in 'read' mode; force single elements to lists
#with open("show_security_zones.xml", "r") as infile:
#    # Use etree.fromstring to read in the file
#    show_security_zones = xmltodict.parse(infile.read(), force_list=True)
#
#
## Using a context manager; open file in 'read' mode; force single elements to lists
#with open("show_security_zones_single_zone.xml", "r") as infile:
#    # Use etree.fromstring to read in the file
#    show_security_zones_single = xmltodict.parse(infile.read(), force_list=True)
#
## Print out the type of the element 'security-zone' in original XML document
#print()
#print("Type of 'security-zone' in original XML file")
#print("-" * 20)
#print(type(show_security_zones["security"][0]["zones"][0]["security-zone"]))
#
## Print out the type of the element 'security-zone' in updated XML document
#print()
#print("Type of 'security-zone' in modified XML file with only one zone")
#print("-" * 20)
#print(type(show_security_zones_single["security"][0]["zones"][0]["security-zone"]))
