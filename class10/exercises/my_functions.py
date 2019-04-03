from netmiko import ConnectHandler
from nxapi_plumbing import Device


def ssh_command(device, command):
    """Establish an SSH connection. Execute show command, return results."""
    device = ConnectHandler(**device)
    output = device.send_command(command)
    device.disconnect()
    print("\n")
    print("-" * 20)
    print(output)
    print("-" * 20)
    print("\n")
    return


def show_version(device):
    """
    Create netmiko device and execute show version
    """
    device = ConnectHandler(**device)
    output = device.send_command("show version")
    print(output)
    return output


def show_version_nxapi(device):
    """
    Create nxapi_plumbing device and execute show version
    """
    device = Device(**device)
    output = device.show("show version")
    print(output)
    return output


def show_version_mapper(device):
    """
    Determine appropriate show function to call based on device type; return output
    """
    device = device.copy()
    device_type = device.pop("connection_type")
    if device_type == "netmiko":
        output = show_version(device)
    elif device_type == "nxapi":
        output = show_version_nxapi(device)
    return output
