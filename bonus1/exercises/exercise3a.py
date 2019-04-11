import os
import requests

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


# Constants
BASE_URL = "https://netbox.lasthop.io/api/"


def main():

    token = os.environ["NETBOX_TOKEN"]

    http_headers = {}
    http_headers["accept"] = "application/json; version=2.4;"
    http_headers["Authorization"] = f"Token {token}"

    # Retrieve all the devices
    resp = requests.get(f"{BASE_URL}dcim/devices/", headers=http_headers, verify=False)

    # Get the JSON results key from our query
    results = resp.json()["results"]

    # Create a list of all our devices with their friendly "display_name"
    devices = []
    for dev in results:
        devices.append(dev["display_name"])

    # Or if you prefer list-comprehensions
    # devices = [dev["display_name"] for dev in results]

    print()
    print(devices)
    print()


if __name__ == "__main__":
    main()
