import os
from getpass import getpass


username = "pyclass"
password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

cisco3 = {
    "hostname": "cisco3.lasthop.io",
    "username": username,
    "password": password,
    "platform": "ios",
}

arista1 = {
    "hostname": "arista1.lasthop.io",
    "username": username,
    "password": password,
    "platform": "eos",
}

nxos1 = {
    "hostname": "nxos1.lasthop.io",
    "username": username,
    "password": password,
    "platform": "nxos",
    "optional_args": {"port": 8443},
}

# List of devices (only cisco3 and arista1)
network_devices = [cisco3, arista1]
