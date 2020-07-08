import time
import re

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

from netmiko import ConnectHandler
from my_devices import nxos1, nxos2


if __name__ == "__main__":
    env = Environment(undefined=StrictUndefined)
    env.loader = FileSystemLoader("./templates/exercise2")

    template_file = "nxos_intf_bgp.j2"
    interface = "Ethernet1/1"

    nxos1_vars = {
        "device_name": "nxos1",
        "local_as": 22,
        "interface": interface,
        "ipv4_address": "10.1.100.1",
        "ipv4_netmask": "24",
    }

    nxos2_vars = {
        "device_name": "nxos2",
        "local_as": 22,
        "interface": interface,
        "ipv4_address": "10.1.100.2",
        "ipv4_netmask": "24",
    }

    nxos1_vars["peer_ip"] = nxos2_vars["ipv4_address"]
    nxos2_vars["peer_ip"] = nxos1_vars["ipv4_address"]

    # Add Jinja2 vars to be included in the Netmiko device dictionary
    nxos1["j2_vars"] = nxos1_vars
    nxos2["j2_vars"] = nxos2_vars

    print()
    for device in (nxos1, nxos2):
        # Create a copy as I am going to modify the dictionary
        tmp_device = device.copy()
        j2_vars = tmp_device.pop("j2_vars")
        template = env.get_template(template_file)
        cfg = template.render(**j2_vars)
        device_name = device["j2_vars"]["device_name"]
        print(f" {device_name} ".center(80, "#"))
        print(f"\n>>> Template output {device_name}")
        print(cfg)
        # Stripping out whitespace will make CLI cfg-output display cleaner
        cfg_lines = [cfg.strip() for cfg in cfg.splitlines()]

        # Establish Netmiko Connection
        net_connect = ConnectHandler(**tmp_device)
        # Store the SSH connection for later (so I don't have to reconnect)
        device["ssh_conn"] = net_connect
        print(f">>> Configuring {device_name}")
        output = net_connect.send_config_set(cfg_lines)
        print(output)
        print("\n\n")

    # Give BGP enough time to reach the established state
    sleep_time = 15
    print(f"Sleeping for {sleep_time} seconds...")
    time.sleep(sleep_time)

    print("\n\n")
    print(">>> Testing ping and BGP")
    for device in (nxos1,):
        net_connect = device["ssh_conn"]
        remote_ip = device["j2_vars"]["peer_ip"]

        # Test ping
        output = net_connect.send_command(f"ping {remote_ip}")
        print(output)
        if "64 bytes from" not in output:
            print("\nPing failed!!!")
        print("\n\n")

        # Test BGP
        bgp_verify = f"show ip bgp summary | include {remote_ip}"
        output = net_connect.send_command(bgp_verify)
        # Retrieve the State/PfxRcd field which is the last field
        match = re.search(r"\s+(\S+)\s*$", output)
        prefix_received = match.group(1)
        try:
            # If this is an integer, the BGP session reached the established state
            int(prefix_received)
            print(
                f"BGP reached the established state. Prefixes received {prefix_received}"
            )
        except ValueError:
            print("BGP failed to reach the established state")

    # All done - disconnect on both devices
    for device in (nxos1, nxos2):
        net_connect = device["ssh_conn"]
        net_connect.disconnect()

    print("\n\n")
