import pyeapi
from getpass import getpass
from my_funcs import yaml_load_devices, output_printer


def main():

    devices = yaml_load_devices()
    password = getpass()

    for name, device_dict in devices.items():
        device_dict["password"] = password
        connection = pyeapi.client.connect(**device_dict)
        device = pyeapi.client.Node(connection)
        output = device.enable("show ip arp")
        arp_list = output[0]["result"]["ipV4Neighbors"]
        output_printer(arp_list)


if __name__ == "__main__":
    main()
