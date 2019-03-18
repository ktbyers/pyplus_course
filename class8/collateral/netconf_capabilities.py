from ncclient import manager
from getpass import getpass
from pprint import pprint

with manager.connect(
    host="srx2.lasthop.io",
    # host="cisco3.lasthop.io",
    port=830,
    username="pyclass",
    password=getpass(),
    hostkey_verify=False,
    allow_agent=False,
    look_for_keys=False,
) as netconf_manager:

    pprint(netconf_manager.server_capabilities.__dict__)
