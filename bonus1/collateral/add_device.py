import os
import requests
import json
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


if __name__ == "__main__":

    token = os.environ["NETBOX_TOKEN"]
    url = "https://netbox.lasthop.io/api/dcim/devices/"
    http_headers = {
        "Content-Type": "application/json",
        "authorization": "Token {}".format(token),
    }
    post_data = {
        "name": "arista8",
        "device_role": 4,  # Distribution Switch
        "device_type": 2,  # vEOS
        "display": "arista8",
        "role": 4,  # Distribution Switch
        "rack": 1,  # RK1
        "site": 2,  # Fremont Data Center
        "status": "active",  # Active
    }

    response = requests.post(
        url, headers=http_headers, data=json.dumps(post_data), verify=False
    )
    response = response.json()
    print()
    pprint(response)
    # print(response._content.decode())
    print()
