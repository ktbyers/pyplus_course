from __future__ import unicode_literals, print_function
from lxml import etree


def read_xml(filename):
    # Encoding in document forces the read to be binary
    with open(filename, "rb") as infile:
        return etree.fromstring(infile.read())


if __name__ == "__main__":
    filename = "show_version.xml"
    show_version = read_xml(filename)

    print("\n\n")
    print("Print default document namespace mapping")
    print("-" * 20)
    print("Document default Namespace:\n {}".format(show_version.nsmap))

    print("\n\n")
    print("Print the proc_board_id element using namespace wildcard")
    print("-" * 20)
    serial_number = show_version.find(".//{*}proc_board_id").text
    print(serial_number)
