#!/usr/bin/env python
import os
from getpass import getpass
from napalm import get_network_driver

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

test_mode = os.getenv("PYNET_PASSWORD")
password = os.getenv("PYNET_PASSWORD") if test_mode else getpass()


def hit_enter():
    if not test_mode:
        input("Hit enter to continue: ")


if __name__ == "__main__":

    host = "nxos1.lasthop.io"
    username = "pyclass"
    optional_args = {"port": 8443}

    driver = get_network_driver("nxos")
    device = driver(host, username, password, optional_args=optional_args)

    print()
    print(">>>Test device open")
    device.open()
    hit_enter()

    print()
    print(">>>Load config change (merge) - no commit")
    device.load_merge_candidate(filename="nxos-merge.conf")
    print(device.compare_config())
    # import ipdb

    # ipdb.set_trace()
    hit_enter()

    print()
    print(">>>Discard config change (merge)")
    device.discard_config()
    print("--- Diff ---")
    print(device.compare_config())
    print("--- End Diff ---")
    hit_enter()

    print()
    print(">>>Load config change (merge) - commit")
    device.load_merge_candidate(filename="nxos-merge.conf")
    # print(device.compare_config())
    device.commit_config()
    hit_enter()

    # print()
    # print(">>>Rollback")
    # device.rollback()
    # hit_enter()
