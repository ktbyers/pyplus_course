import os
import yaml

# Check if in "test" mode or not
if os.getenv("PYNET_PASSWORD"):
    filename = "test4.yml"
else:
    filename = input("Enter filename: ")

# pyyaml made a backwards incompatible change to .load()
# the simple fix is just to call .safe_load() instead
with open(filename) as f:
    yaml_out = yaml.safe_load(f)
print(yaml_out)
