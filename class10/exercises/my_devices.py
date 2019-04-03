from getpass import getpass


username = "pyclass"
password = getpass()

cisco3 = {
    "host": "cisco3.lasthop.io",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

arista1 = {
    "host": "arista1.lasthop.io",
    "username": username,
    "password": password,
    "device_type": "arista_eos",
    "global_delay_factor": 4,
}

srx2 = {
    "host": "srx2.lasthop.io",
    "username": username,
    "password": password,
    "device_type": "juniper_junos",
}

network_devices = [cisco3, arista1, srx2]
