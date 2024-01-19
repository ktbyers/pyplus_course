import os
import requests
import json
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


if __name__ == "__main__":
    """
    HTTP PUT
    URL: https://netbox.lasthop.io/api/dcim/devices/8/
    HTTP Headers: {'Content-Type': 'application/json', 'authorization': 'Token x'}
    PUT DATA: {'id': 8, 'name': 'arista6', 'display_name': 'arista6', 'device_type': 2,
    'device_role': 3, 'tenant': None, 'platform': 4, 'serial': '', 'asset_tag': None,
    'site': 1, 'rack': 2, 'position': None,
    'face': None, 'parent_device': None, 'status': 1, 'primary_ip': None, 'primary_ip4': None,
    'primary_ip6': None, 'cluster': None, 'virtual_chassis': None, 'vc_position': None,
    'vc_priority': None, 'comments': '', 'tags': [], 'custom_fields': {}, 'created': '2018-11-01',
    'last_updated': '2018-11-01T12:29:41.716417-07:00', 'local_context_data': None}
    """

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
