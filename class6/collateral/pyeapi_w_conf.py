import pyeapi

device1 = pyeapi.connect_to("arista8")
device2 = pyeapi.connect_to("arista7")
print(device1)
