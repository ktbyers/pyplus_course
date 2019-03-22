from my_functions import open_napalm_connection
from my_devices import network_devices


if __name__ == "__main__":

    connections = []
    for device in network_devices:
        conn = open_napalm_connection(device)
        connections.append(conn)

    for conn in connections:
        print("\n\n")
        print("-" * 20)
        # Stage configurations
        conn.load_merge_candidate(filename="{}-loopbacks".format(conn.hostname))
        print("Diff before commiting for device {}".format(conn.hostname))
        diff = conn.compare_config()
        print(">" * 8)
        print(diff)
        print(">" * 8)
        if diff:
            conn.commit_config()
        print("\nDiff after commiting for device {}".format(conn.hostname))
        print(">" * 8)
        print(conn.compare_config())
        print(">" * 8)
        conn.close()
    print("\n\n")
