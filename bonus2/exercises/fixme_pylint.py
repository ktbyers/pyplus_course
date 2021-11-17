"""Pylint Exercise - clean code."""
from pprint import pprint
from napalm import get_network_driver
from my_devices import network_devices


def open_napalm_connection(device):
    """Funtion to open napalm connection and return connection object"""
    # Copy dictionary to ensure original object is not modified
    device = device.copy()
    # Pop "platform" as this is an invalid kwarg to napalm
    platform = device.pop("platform")
    driver = get_network_driver(platform)
    conn = driver(**device)
    conn.open()
    return conn


def main():
    """Pylint Exercise - clean code."""
    connections = []
    for device in network_devices:
        conn = open_napalm_connection(device)
        connections.append(conn)

    print("\n\n")
    print("Print facts for all devices in connections list")
    print("-" * 20)
    for conn in connections:
        print()
        print("-" * 6)
        print(conn)
        pprint(f"{conn.platform} facts:")
        pprint(conn.get_facts())
        print("-" * 6)
        # Close the NAPALM connection
        conn.close()
    print("\n\n")


if __name__ == "__main__":
    main()
