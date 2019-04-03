from netmiko import ConnectHandler


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


def ssh_command2(device, command):
    """Establish an SSH connection. Execute show command, return results."""
    device = ConnectHandler(**device)
    output = device.send_command(command)
    device.disconnect()
    return output
