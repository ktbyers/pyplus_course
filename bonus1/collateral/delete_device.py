import os
import sys
import requests

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


def find_device_id():
    """
    Helper function so that automated tests work.

    Automatically find the device 'id'
    """
    token = os.environ["NETBOX_TOKEN"]
    url = "https://netbox.lasthop.io/api/dcim/devices/"
    http_headers = {"accept": "application/json"}
    if token:
        http_headers["authorization"] = "Token {}".format(token)
    response = requests.get(url, headers=http_headers, verify=False)
    response = response.json()
    for device_entry in response["results"]:
        if device_entry["name"] == "arista8":
            return device_entry["id"]
    return None


if __name__ == "__main__":

    token = os.environ["NETBOX_TOKEN"]

    # Will need updated to map to arista8 that is created via add_device.py
    device_id = find_device_id()
    if device_id and int(device_id):
        url = f"https://netbox.lasthop.io/api/dcim/devices/{device_id}/"
    else:
        sys.exit("Could not find the device_id automatically")

    http_headers = {
        "Content-Type": "application/json",
        "authorization": "Token {}".format(token),
    }

    response = requests.delete(url, headers=http_headers, verify=False)

    if response.ok:
        print("Device deleted successfully")
