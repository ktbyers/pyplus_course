from pprint import pprint
import sys

from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
from jnpr.junos.op.arp import ArpTable

from lesson2_devices import junos_devices


def check_connected(device):
    if dev.connected:
        print(f"Device {dev.hostname} is connected!")
    else:
        print(f"Device {dev.hostname} failed to connect :(.")
        # If device is *not* connected; exit script
        sys.exit(1)


def gather_routes(device):
    # Create RouteTable view object
    routes = RouteTable(device)
    # Get all routes
    routes.get()
    return routes


def gather_arps(device):
    # Create ArpTable view object
    arp = ArpTable(dev)
    # Get all arp information
    arp.get()
    return arp


# Function to print out desired data from zip of device, route and arp information
def print_beautiful_output(device_info):
    # iterate through a list of the zipped objects
    print()
    print("Print out desired output from device, route, and arp information")
    print("-" * 20)
    #for dev in list(device_info):
    for dev in device_info:
        # Create device dictionary and assign desired values
        device = {}
        device["hostname"] = dev[0].hostname
        device["connected_port"] = dev[0].port
        device["connected_user"] = dev[0].user
        device["route_table"] = dev[1].items()
        device["arp_table"] = dev[2].items()
        # Pretty print device dictionary
        pprint(device)


if __name__ == "__main__":

    devices = []
    for dev in junos_devices:
        dev = Device(**dev)
        dev.open()
        devices.append(dev)

    routes = []
    arps = []
    for dev in devices:
        check_connected(dev)
        routes.append(gather_routes(dev))
        arps.append(gather_arps(dev))

    # Zip devices, routes, and arps together
    device_info = zip(devices, routes, arps)
    import pdb
    pdb.set_trace()
    # Pass zipped data to print function for parsing
    print_beautiful_output(device_info)
