from getpass import getpass


username = "pyclass"
password = getpass()

# Dictionary to define cisco3 and arista1 devices
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

# List of all devices
network_devices = [cisco3, arista1]
