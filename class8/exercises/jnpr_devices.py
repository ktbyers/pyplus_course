import os
from getpass import getpass

username = "pyclass"
password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

# Dictionary to define each SRX device
srx2 = {"host": "srx2.lasthop.io", "user": username, "password": password}

# List of all SRX devices
junos_devices = [srx2]
