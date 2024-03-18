#!/usr/bin/env python
import os
from getpass import getpass
from napalm import get_network_driver

test_mode = os.getenv("PYNET_PASSWORD")
password = os.getenv("PYNET_PASSWORD") if test_mode else getpass()


def hit_enter():
    if not test_mode:
        input("Hit enter to continue: ")


if __name__ == "__main__":
    host = "cisco3.lasthop.io"
    username = "pyclass"
    # optional_args = {}
    optional_args = {"inline_transfer": True}

    driver = get_network_driver("ios")
    device = driver(host, username, password, optional_args=optional_args)

    print()
    print(">>>Test device open")
    device.open()
    hit_enter()

    print()
    print(">>>Load config change (replace)")
    device.load_replace_candidate(filename="cisco3.txt")
    print(device.compare_config())
    # device.discard_config()
    # device.commit_config()
    # device.rollback()
    hit_enter()
