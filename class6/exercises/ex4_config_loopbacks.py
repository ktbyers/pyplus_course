import os
import pyeapi
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from getpass import getpass
from my_funcs import yaml_load_devices


if __name__ == "__main__":
    password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

    env = Environment(undefined=StrictUndefined)
    env.loader = FileSystemLoader(".")
    template_file = "loopback_intf.j2"

    yaml_out = yaml_load_devices("arista_devices_full.yml")
    my_devices = yaml_out["my_devices"]

    eapi_devices = []
    for device_name in my_devices:
        device_dict = yaml_out[device_name]
        device_dict["password"] = password

        # Generate config from template
        j2_vars = device_dict.pop("data")
        template = env.get_template(template_file)
        cfg_lines = template.render(**j2_vars)
        cfg_lines = cfg_lines.strip()
        cfg_lines = cfg_lines.splitlines()

        # Establish eAP connection and push config
        eapi_conn = pyeapi.client.connect(**device_dict)
        device_obj = pyeapi.client.Node(eapi_conn)
        eapi_devices.append(device_obj)
        output = device_obj.config(cfg_lines)
        print(output)

    # Verify interfaces
    for device_obj in eapi_devices:
        output = device_obj.enable("show ip interface brief")
        print()
        print("-" * 50)
        print(output[0]["result"]["output"].rstrip())
        print("-" * 50)
    print()
