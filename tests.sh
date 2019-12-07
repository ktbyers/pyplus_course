#!/bin/bash
pylama .
black --check .
cd tests
py.test -s -v test_bonus2.py
py.test -s -v ../bonus2/exercises/test_ex3/test_simple.py
py.test -s -v ../bonus2/exercises/test_ex4/test_netmiko.py
py.test -s -v ../bonus2/exercises/test_ex5/test_netmiko_conftest.py
