import os
import requests
import json
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


if __name__ == "__main__":

    token = os.environ["NETBOX_TOKEN"]

    # Arista6
    url = "https://netbox.lasthop.io/api/dcim/devices/6/"
    http_headers = {
        "accept": "application/json",
        "authorization": "Token {}".format(token),
    }
    response = requests.get(url, headers=http_headers, verify=False)
    arista6 = response.json()

    http_headers = {
        "Content-Type": "application/json",
        "authorization": "Token {}".format(token),
    }

    # Reformat to get the proper structure for the existing object
    # Only use "id" for these fields (strange Netbox requires this)
    for field in ["device_type", "site", "role"]:
        arista6[field] = {"id": arista6[field]["id"]}
    # Status field is also not happy if we return what the "get" yielded
    # so set to what we originally used when creating the device.
    arista6["status"] = "active"

    # Change the "rack"
    arista6["rack"] = {"id": 2}
    pprint(arista6)

    response = requests.put(
        url, headers=http_headers, data=json.dumps(arista6), verify=False
    )
    response = response.json()
    print()
    pprint(response)
    # print(response._content.decode())
    print()
