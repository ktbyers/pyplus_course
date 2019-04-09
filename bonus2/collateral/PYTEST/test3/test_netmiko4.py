def test_find_prompt(netmiko_conn):
    assert "cisco3#" in netmiko_conn.find_prompt()


def test_send_command(netmiko_conn):
    output = netmiko_conn.send_command("show ip int brief")
    assert "10.220.88.22" in output
