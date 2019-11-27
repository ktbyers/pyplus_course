import os
import pyeapi
from getpass import getpass
from my_funcs import yaml_load_devices

if __name__ == "__main__":
    password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

    devices = yaml_load_devices()

    for name, device_dict in devices.items():
        device_dict["password"] = password
        connection = pyeapi.client.connect(**device_dict)
        device = pyeapi.client.Node(connection)
        output = device.enable("show ip route")
        routes = output[0]["result"]["vrfs"]["default"]["routes"]

        print()
        for prefix, route_dict in routes.items():
            route_type = route_dict["routeType"]
            print()
            print(prefix)
            print("-" * 12)
            print(route_type)
            print(">" * 6)
            print(route_dict["vias"][0]["interface"])
            if route_type == "static":
                print(route_dict["vias"][0]["nexthopAddr"])
            print("-" * 12)

        print()
