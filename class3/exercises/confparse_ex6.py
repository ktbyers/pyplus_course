import yaml
from os import path
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse


if __name__ == "__main__":
    home_dir = path.expanduser("~")
    filename = path.join(home_dir, ".netmiko.yml")

    with open(filename) as f:
        yaml_out = yaml.safe_load(f)

    device = yaml_out["cisco4"]
    net_connect = ConnectHandler(**device)
    show_run = net_connect.send_command("show run")

    # When feeding config directly - CiscoConfParse requires a list
    cisco_cfg = CiscoConfParse(show_run.splitlines())
    interfaces = cisco_cfg.find_objects_w_child(
        parentspec=r"^interface", childspec=r"^\s+ip address"
    )

    print()
    for intf in interfaces:
        print("Interface Line: {}".format(intf.text))
        ip_address = intf.re_search_children(r"ip address")[0].text
        print("IP Address Line: {}".format(ip_address))
        print()
    print()
