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
    HTTP Headers: {'Content-Type': 'application/json; version=2.4;',
        'authorization': 'Token aaaabbbbccccddddeeeeffff0000111122223333'}
    POST DATA: {'name': 'arista4', 'device_role': 3, 'device_type': 2, 'display_name': 'arista4',
        'platform': 4, 'rack': 1, 'site': 1, 'status': 1}
    --------------------------------------------------------------------------------
    """

    token = os.environ["NETBOX_TOKEN"]
    url = "https://netbox.lasthop.io/api/dcim/devices/"
    http_headers = {
        "Content-Type": "application/json; version=2.4;",
        "authorization": "Token {}".format(token),
    }
    post_data = {
        "name": "arista8",
        "device_role": 3,  # Distribution Switch
        "device_type": 2,  # vEOS
        "display_name": "arista8",
        "platform": 4,  # Arista EOS
        "rack": 1,  # RK1
        "site": 1,  # Fremont Data Center
        "status": 1,  # Active
    }

    response = requests.post(
        url, headers=http_headers, data=json.dumps(post_data), verify=False
    )
    response = response.json()
    print()
    pprint(response)
    # print(response._content.decode())
    print()
