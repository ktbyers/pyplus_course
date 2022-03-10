import yaml

# pyyaml made a backwards incompatible change to .load()
# the simple fix is just to call .safe_load() instead
filename = input("Enter filename: ")
with open(filename) as f:
    yaml_out = yaml.safe_load(f)
print(yaml_out)
