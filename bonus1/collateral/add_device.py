import os
import requests
import json
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


if __name__ == "__main__":
    """
    --------------------------------------------------------------------------------
    HTTP POST
    URL: https://netbox.lasthop.io/api/dcim/devices/
    HTTP Headers: {'Content-Type': 'application/json',
        'authorization': 'Token aaaabbbbccccddddeeeeffff0000111122223333'}
    POST DATA: {'name': 'arista4', 'device_role': 3, 'device_type': 2, 'display_name': 'arista4',
        'platform': 4, 'rack': 1, 'site': 1, 'status': 1}
    --------------------------------------------------------------------------------
    """

    token = os.environ["NETBOX_TOKEN"]
    url = "https://netbox.lasthop.io/api/dcim/devices/"
    http_headers = {
        "Content-Type": "application/json",
        "authorization": "Token {}".format(token),
    }
    post_data = {
        "name": "arista8",
        "device_role": {"id": 4},  # Distribution Switch
        "device_type": {"id": 2},  # vEOS
        "display": "arista8",
        "role": {"id": 4},  # Distribution Switch
        "rack": {"id": 1},  # RK1
        "site": {"id": 2},  # Fremont Data Center
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
