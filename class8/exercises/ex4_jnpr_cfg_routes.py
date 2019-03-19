from jnpr.junos import Device
from jnpr.junos.utils.config import Config

from jnpr_devices import srx2
from ex2_jnpr_tables import check_connected, gather_routes


# Constant var pointing to configuration file
CONFIG_FILE = "static_routes.conf"


def config_from_file(path, dev, merge=True):
    """Function to load config from file and commit it to a device."""
    # Create Config object
    cfg = Config(dev)
    cfg.lock()
    # Load configuration from file; default to merge operation
    cfg.load(path=path, format="text", merge=merge)
    if cfg.diff() is not None:
        cfg.commit()
    cfg.unlock()


def compare_routes(initial_routes, updated_routes):
    """Function to compare two route views."""
    print()
    print("Check for newly added routes")
    print("-" * 20)
    new_routes = []
    for route in updated_routes.keys():
        if route not in initial_routes.keys():
            new_routes.append(route)
    return new_routes


def cleanup_routes(dev):
    """Remove the static routes that were added in this exercise."""
    # Create Config object
    cfg = Config(dev)
    cfg.lock()
    # Use set format to delete previously created static routes
    cfg.load(
        "delete routing-options static route 203.0.113.5/32", format="set", merge=True
    )
    cfg.load(
        "delete routing-options static route 203.0.113.200/32", format="set", merge=True
    )
    print()
    print("Cleaning up routes that were added in this exercise.")
    print("\n\n")
    if cfg.diff() is not None:
        cfg.commit()
    cfg.unlock()


if __name__ == "__main__":

    # Open device connections
    device = Device(**srx2)
    device.open()
    check_connected(device)

    # Call function to gather routes
    routes = gather_routes(device)

    # Configure route changes on device
    config_from_file(CONFIG_FILE, device)

    # Call function to gather route
    updated_routes = gather_routes(device)

    # Call function to compare two route table views
    new_routes = compare_routes(routes, updated_routes)
    print(f"{device.hostname} has the following NEW routes: {new_routes}")

    cleanup_routes(device)
