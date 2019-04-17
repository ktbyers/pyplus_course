def test_prompt(netmiko_connect):
    """Simple test to test netmiko "find_prompt"""
    assert netmiko_connect.find_prompt() == "arista1#"


def test_show_version(netmiko_connect):
    """Simple test to test netmiko "show_version"""
    assert "4.20.10M" in netmiko_connect.send_command("show version")
