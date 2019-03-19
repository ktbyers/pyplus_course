from pprint import pprint
import sys

from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
from jnpr.junos.op.arp import ArpTable

from jnpr_devices import srx2


def check_connected(device):
    print("\n\n")
    if device.connected:
        print(f"Device {device.hostname} is connected!")
    else:
        print(f"Device {device.hostname} failed to connect :(.")
        # If device is *not* connected; exit script
        sys.exit(1)


def gather_routes(device):
    # Create RouteTable view object
    routes = RouteTable(device)
    # Get all routes
    routes.get()
    return routes


def gather_arp_table(device):
    # Create ArpTable view object
    arp = ArpTable(device)
    # Get all arp information
    arp.get()
    return arp


def print_output(dev, routes, arp):
    print()
    print("Print out desired output from device, route, and arp information")
    print("-" * 20)
    device = {}
    device["hostname"] = dev.hostname
    device["connected_port"] = dev.port
    device["connected_user"] = dev.user
    device["route_table"] = routes.items()
    device["arp_table"] = arp.items()
    pprint(device)
    print()


if __name__ == "__main__":

    device = Device(**srx2)
    device.open()

    check_connected(device)
    routes = gather_routes(device)
    arp = gather_arp_table(device)

    print_output(device, routes, arp)
