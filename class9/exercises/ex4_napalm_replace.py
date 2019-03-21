from my_functions import open_napalm_connection, create_checkpoint
from my_devices import nxos1


NXOS_REPLACE_CANDIDATE = "nxos1_replacement_cfg"


if __name__ == "__main__":
    conn = open_napalm_connection(nxos1)

    # Create a checkpoint from the current configuration
    create_checkpoint(conn)

    print("\n\n")
    print("Diff before and after loading replace candidate: nxos only")
    print("-" * 20)
    conn.load_replace_candidate(NXOS_REPLACE_CANDIDATE)
    print("Diff before commiting for device {}".format(conn.hostname))
    print(">" * 8)
    print(conn.compare_config())
    print(">" * 8)

    print("\nDiscarding candidate config for device {}".format(conn.hostname))
    conn.discard_config()
    print("Diff after discarding candidate config for device {}".format(conn.hostname))
    print(">" * 8)
    print(conn.compare_config())
    print(">" * 8)
