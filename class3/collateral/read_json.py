import json
from pprint import pprint

filename = input("Input filename: ")
with open(filename) as f:
    data = json.load(f)
pprint(data)
