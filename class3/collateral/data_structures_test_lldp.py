from pprint import pprint

lldp = {
    "Eth2/1": [
        {
            "remote_chassis_id": "2C:C2:60:54:DC:2C",
            "parent_interface": "",
            "remote_port": "Ethernet2/1",
            "remote_port_description": "Ethernet2/1",
            "remote_system_name": "nxos2.twb-tech.com",
            "remote_system_description": "Cisco NX-OS(tm) titanium, Software (titanium-d1), Version 7.3(1)D1(1), Interim version 7.3(1)D1(0.10), RELEASE SOFTWARE Copyright (c) 2002-2013, 2015 by Cisco Systems, Inc. Compiled 1/11/2016 16:00:00",
            "remote_system_capab": "B, R",
            "remote_system_enable_capab": "B, R",
        }
    ],
    "Eth2/2": [
        {
            "remote_chassis_id": "2C:C2:60:64:E1:5F",
            "parent_interface": "",
            "remote_port": "Ethernet2/2",
            "remote_port_description": "Ethernet2/2",
            "remote_system_name": "nxos2.twb-tech.com",
            "remote_system_description": "Cisco NX-OS(tm) titanium, Software (titanium-d1), Version 7.3(1)D1(1), Interim version 7.3(1)D1(0.10), RELEASE SOFTWARE Copyright (c) 2002-2013, 2015 by Cisco Systems, Inc. Compiled 1/11/2016 16:00:00",
            "remote_system_capab": "B, R",
            "remote_system_enable_capab": "B, R",
        }
    ],
    "Eth2/3": [
        {
            "remote_chassis_id": "2C:C2:60:72:61:7B",
            "parent_interface": "",
            "remote_port": "Ethernet2/3",
            "remote_port_description": "Ethernet2/3",
            "remote_system_name": "nxos2.twb-tech.com",
            "remote_system_description": "Cisco NX-OS(tm) titanium, Software (titanium-d1), Version 7.3(1)D1(1), Interim version 7.3(1)D1(0.10), RELEASE SOFTWARE Copyright (c) 2002-2013, 2015 by Cisco Systems, Inc. Compiled 1/11/2016 16:00:00",
            "remote_system_capab": "B, R",
            "remote_system_enable_capab": "B, R",
        }
    ],
    "Eth2/4": [
        {
            "remote_chassis_id": "2C:C2:60:70:69:DA",
            "parent_interface": "",
            "remote_port": "Ethernet2/4",
            "remote_port_description": "Ethernet2/4",
            "remote_system_name": "nxos2.twb-tech.com",
            "remote_system_description": "Cisco NX-OS(tm) titanium, Software (titanium-d1), Version 7.3(1)D1(1), Interim version 7.3(1)D1(0.10), RELEASE SOFTWARE Copyright (c) 2002-2013, 2015 by Cisco Systems, Inc. Compiled 1/11/2016 16:00:00",
            "remote_system_capab": "B, R",
            "remote_system_enable_capab": "B, R",
        }
    ],
}

new_list = []
for intf_name, lldp_data in lldp.items():
    lldp_data = lldp_data[0]
    new_entry = {"intf_name": intf_name, "remote_port": lldp_data["remote_port"]}
    new_list.append(new_entry)

print()
pprint(new_list)
print()
