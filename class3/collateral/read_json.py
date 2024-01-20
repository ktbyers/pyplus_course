import os
import json
from pprint import pprint

# Check if in "test" mode or not
if os.getenv("PYNET_PASSWORD"):
    filename = "outfile.json"
else:
    filename = input("Input filename: ")

with open(filename) as f:
    data = json.load(f)
pprint(data)
