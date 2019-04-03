from concurrent.futures import ProcessPoolExecutor, as_completed
import time
from my_devices import network_devices
from my_functions import ssh_command2


def main():
    """
    Use concurrent futures threading to simultaneously gather "show version" output from devices.
    Wait for all threads to complete. Record the amount of time required to do this.
    """
    start_time = time.time()
    max_procs = 5

    # Create the process pool
    with ProcessPoolExecutor(max_procs) as pool:

        # Create list to append the processes to
        futures = []
        for device in network_devices:
            futures.append(pool.submit(ssh_command2, device, "show version"))

        print("\n\n")
        for future in as_completed(futures):
            print("-" * 40)
            print("Result: " + future.result())
            print("-" * 40)
            print("\n\n")

        end_time = time.time()
        print(f"Finished in {end_time - start_time:.2f}")
        print("\n\n")


if __name__ == "__main__":
    main()
