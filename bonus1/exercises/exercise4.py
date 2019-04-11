import os
import json
import requests
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


# Constants
BASE_URL = "https://netbox.lasthop.io/api/"


def main():

    token = os.environ["NETBOX_TOKEN"]

    # HTTP POST needs the "Content-Type" header instead of "accept"
    http_headers = {}
    http_headers["Content-Type"] = "application/json; version=2.4;"
    http_headers["accept"] = "application/json; version=2.4;"
    http_headers["Authorization"] = f"Token {token}"

    # Required IP Address data
    data = {"address": "192.0.2.231/32"}

    # POST the data to Netbox
    resp = requests.post(
        f"{BASE_URL}ipam/ip-addresses/",
        headers=http_headers,
        verify=False,
        data=json.dumps(data),
    )
    print()
    print("Creating IP address object:")
    print(f"Response code: {resp.status_code}")
    print("Returned JSON:")
    print("-" * 12)
    pprint(resp.json())

    # Retrieve the new object ID and query that specific object
    print()
    print("Query newly created object...")
    address_id = resp.json()["id"]

    # New URL specific to our new IP address object
    url = f"{BASE_URL}ipam/ip-addresses/{address_id}/"
    resp = requests.get(url, headers=http_headers, verify=False)
    print("-" * 12)
    pprint(resp.json())

    print()
    print(f"IP Addreses ID: {address_id}")
    print()


if __name__ == "__main__":
    main()
