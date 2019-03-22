from my_functions import open_napalm_connection, create_checkpoint
from my_devices import nxos1

# Disable Self-signed Certificate Warnings
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


NXOS_REPLACE_CANDIDATE = "nxos1_replacement_cfg"


if __name__ == "__main__":
    conn = open_napalm_connection(nxos1)

    # Create a checkpoint from the current configuration
    create_checkpoint(conn)

    print("\n\n")
    conn.load_replace_candidate(NXOS_REPLACE_CANDIDATE)
    print("Config staged: pending differences {}".format(conn.hostname))
    print(">" * 8)
    print(conn.compare_config())
    print(">" * 8)

    print("\n\n")
    print("Discarding candidate config for device {}".format(conn.hostname))
    conn.discard_config()
    print("Diff after discarding candidate config for device {}".format(conn.hostname))
    print(">" * 8)
    print(conn.compare_config())
    print(">" * 8)
    print("\n\n")
    conn.close()
