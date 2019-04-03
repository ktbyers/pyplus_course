import time
import threading
from my_devices import network_devices
from my_functions import ssh_command


def main():
    """
    Use "legacy" threading to gather "show version" from the devices.
    Record the total time required to do this.
    """
    start_time = time.time()

    # Create list to append threads to
    threads = []

    # Start each of the threads
    print("\n\n")
    for device in network_devices:
        t = threading.Thread(target=ssh_command, args=(device, "show version"))
        threads.append(t)
        t.start()

    # Iterate through threads and wait for all to complete
    for t in threads:
        t.join()

    end_time = time.time()
    print("\n\n")
    print(f"Finished in {end_time - start_time:.2f}")
    print("\n\n")


if __name__ == "__main__":
    main()
