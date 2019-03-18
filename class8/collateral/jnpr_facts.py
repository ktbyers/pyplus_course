from jnpr.junos import Device
from getpass import getpass
from pprint import pprint

a_device = Device(host="srx2.lasthop.io", user="pyclass", password=getpass())
a_device.open()
pprint(a_device.facts)
