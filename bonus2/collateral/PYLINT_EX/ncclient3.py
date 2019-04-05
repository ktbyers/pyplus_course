"""Test code that is testing NETCONF."""
from getpass import getpass
import ipdb
from ncclient import manager
from ncclient.xml_ import new_ele


def main():
    """Test code that is testing NETCONF."""
    conn = manager.connect(
        host="srx2.lasthop.io",
        username="pyclass",
        password=getpass(),
        device_params={"name": "junos"},
        hostkey_verify=False,
        allow_agent=False,
        look_for_keys=False,
        port=830,
        timeout=60,
    )

    ipdb.set_trace()
    rpc = new_ele("get-software-information")
    nc_out = conn.rpc(rpc)

    # It is an XML like thing
    print(nc_out.tostring.decode())
    print(nc_out.find(".//product-name"))
    print(nc_out.find(".//product-name").text)
    print(nc_out.find(".//product-model").text)

    config = conn.get_config(source="running")
    config_xml = config.data_xml
    print(config_xml)


if __name__ == "__main__":
    main()
