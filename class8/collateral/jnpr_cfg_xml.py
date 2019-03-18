from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from getpass import getpass

a_device = Device(host="srx2.lasthop.io", user="pyclass", password=getpass())
a_device.open()
a_device.timeout = 60

cfg = Config(a_device)
cfg.lock()

cfg.load(path="test_config.xml", format="xml", merge=True)
# overwrite=True - full configuration replace so be careful
# cfg.commit(confirm=1)
# cfg.commit()
# cfg.unlock()
