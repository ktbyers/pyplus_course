import os
import requests

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


if __name__ == "__main__":

    token = os.environ["NETBOX_TOKEN"]

    # Will need updated to map to arista8 that is created via add_device.py
    url = "https://netbox.lasthop.io/api/dcim/devices/11/"

    http_headers = {
        "Content-Type": "application/json",
        "authorization": "Token {}".format(token),
    }

    response = requests.delete(url, headers=http_headers, verify=False)

    if response.ok:
        print("Device deleted successfully")
