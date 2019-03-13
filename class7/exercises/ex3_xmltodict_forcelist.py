from __future__ import unicode_literals, print_function
import xmltodict


def read_xml_forcelist(filename, force_list=None):
    if force_list is None:
        force_list = {}
    with open(filename, "r") as infile:
        return xmltodict.parse(infile.read(), force_list=force_list)


def read_xml(filename):
    with open(filename, "r") as infile:
        return xmltodict.parse(infile.read())


if __name__ == "__main__":

    filename = "show_security_zones.xml"
    show_security_zones = read_xml(filename)

    filename = "show_security_zones_trust.xml"
    show_security_zones_single = read_xml(filename)

    print("\n\n")
    print("Type of 'zones-security' in the first XML file:")
    print("-" * 20)
    print(type(show_security_zones["zones-information"]["zones-security"]))

    print("\n\n")
    print("Type of 'zones-security' in the single-zone XML file:")
    print("-" * 20)
    print(type(show_security_zones_single["zones-information"]["zones-security"]))

    print("\n\n")
    print("Type of 'zones-security' in the single-zone XML file using force_list:")
    print("-" * 20)
    filename = "show_security_zones_trust.xml"
    show_security_zones_single = read_xml_forcelist(
        filename, force_list={"zones-security": True}
    )
    print(type(show_security_zones_single["zones-information"]["zones-security"]))
    print("\n\n")
