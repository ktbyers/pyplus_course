import yaml

my_data = {
    "device_name": "rtr1",
    "ip_addr": "10.1.1.1",
    "username": "admin",
    "password": "foo",
}

some_list = list(range(10))
my_data["some_list"] = some_list
my_data["null_value"] = None
my_data["a_bool"] = False

filename = "outfile.yml"
with open(filename, "wt") as f:
    yaml.dump(my_data, f, default_flow_style=True)
