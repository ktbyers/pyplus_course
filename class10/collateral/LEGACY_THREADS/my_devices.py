from getpass import getpass


std_pwd = getpass()

cisco3 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": std_pwd,
}

cisco4 = {
    "device_type": "cisco_ios",
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": std_pwd,
}

arista1 = {
    "device_type": "arista_eos",
    "host": "arista1.lasthop.io",
    "username": "pyclass",
    "password": std_pwd,
    "global_delay_factor": 4,
}

arista2 = {
    "device_type": "arista_eos",
    "host": "arista2.lasthop.io",
    "username": "pyclass",
    "password": std_pwd,
    "global_delay_factor": 4,
}

arista3 = {
    "device_type": "arista_eos",
    "host": "arista3.lasthop.io",
    "username": "pyclass",
    "password": std_pwd,
    "global_delay_factor": 4,
}

arista4 = {
    "device_type": "arista_eos",
    "host": "arista4.lasthop.io",
    "username": "pyclass",
    "password": std_pwd,
    "global_delay_factor": 4,
}

srx2 = {
    "device_type": "juniper_junos",
    "host": "srx2.lasthop.io",
    "username": "pyclass",
    "password": std_pwd,
}

nxos1 = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": std_pwd,
}

nxos2 = {
    "device_type": "cisco_nxos",
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": std_pwd,
}


device_list = [cisco3, cisco4, arista1, arista2, arista3, arista4, srx2, nxos1, nxos2]
