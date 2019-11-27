import os
from getpass import getpass

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()


nxos1 = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
}

nxos2 = {
    "device_type": "cisco_nxos",
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
}
