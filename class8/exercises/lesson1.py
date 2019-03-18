from getpass import getpass
from pprint import pprint
from jnpr.junos import Device


# Create pyez Device object for srx2
my_dev = Device(host="srx2.lasthop.io", user="pyclass", password=getpass())

# Create NETCONF connection to device
my_dev.open()

print()
print("Print device facts")
print("-" * 20)
pprint(my_dev.facts)

print("\n\n")
print("Print hostname from device facts")
print("-" * 20)
print(my_dev.facts["hostname"])
print()
