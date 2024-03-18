import os

# import ipdb
from ncclient import manager
from getpass import getpass

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

conn = manager.connect(
    host="srx2.lasthop.io",
    username="pyclass",
    password=password,
    device_params={"name": "junos"},
    hostkey_verify=False,
    allow_agent=False,
    look_for_keys=False,
    port=830,
    timeout=60,
)

# ipdb.set_trace()
config = conn.get_config(source="running")
config_xml = config.data_xml
print(config_xml)
