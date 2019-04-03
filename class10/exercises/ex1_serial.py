import time
from netmiko import ConnectHandler
from my_devices import network_devices


def ssh_command(device, command):
    """Establish an SSH connection. Execute show command, return results."""
    device = ConnectHandler(**device)
    output = device.send_command(command)
    device.disconnect()
    return output


def main():
    """
    Serially gather show version output from devices. Record the amount of time required to do
    this.
    """
    start_time = time.time()
    for device in network_devices:
        output = ssh_command(device, "show version")
        print("\n\n")
        print("-" * 20)
        print(output)
        print("-" * 20)
    print("\n\n")
    end_time = time.time()
    print(f"Finished in {end_time - start_time:.2f} seconds")
    print("\n\n")


if __name__ == "__main__":
    main()
