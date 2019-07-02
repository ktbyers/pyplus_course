import os
import requests

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


# Constants
BASE_URL = "https://netbox.lasthop.io/api/"
# MY_IP_ID = "51"
ADDRESS_ID = input("Enter Address ID that was created in exercise4: ")


def main():

    token = os.environ["NETBOX_TOKEN"]

    # HTTP delete needs the "Content-Type" header instead of "accept"
    http_headers = {}
    http_headers["Content-Type"] = "application/json; version=2.4;"
    http_headers["accept"] = "application/json; version=2.4;"
    http_headers["Authorization"] = f"Token {token}"

    # Delete our previously created IP address
    print()
    print("Deleting IP address object.")
    resp = requests.delete(
        f"{BASE_URL}ipam/ip-addresses/{ADDRESS_ID}/", headers=http_headers, verify=False
    )
    print(f"Response code: {resp.status_code}")
    print()


if __name__ == "__main__":
    main()
