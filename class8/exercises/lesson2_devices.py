from getpass import getpass

username = "pyclass"
password = getpass()

# Dictionary to define each SRX device
srx1 = {"host": "srx1.lasthop.io", "user": username, "password": password}
srx2 = {"host": "srx2.lasthop.io", "user": username, "password": password}

# List of all SRX devices
junos_devices = [srx1, srx2]
