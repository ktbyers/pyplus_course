from pprint import pprint
import requests

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


# Constants
BASE_URL = "https://netbox.lasthop.io/api/"


def main():

    # Get top level endpoints
    resp = requests.get(BASE_URL, verify=False)

    print(f"Response Code: {resp.status_code}")
    print()
    print("Response Text:")
    pprint(resp.text)
    print()

    print("Response JSON:")
    pprint(resp.json())
    print()
    print("Response Headers:")
    print(resp.headers)

    print()
    print("Building headers manually")
    headers = {}
    headers["API-Version"] = "2.4"
    headers["Content-Type"] = "application/json"
    resp = requests.get(BASE_URL, headers=headers, verify=False)
    print(resp.text)

    # Get endpoints of DCIM
    print()
    print("Getting all child endpoints of DCIM")
    resp = requests.get(f"{BASE_URL}dcim/", headers=headers, verify=False)
    print("Child endpoints under DCIM:")
    print(*resp.json().keys(), sep="\n")


if __name__ == "__main__":
    main()
