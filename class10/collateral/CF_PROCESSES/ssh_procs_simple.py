import time
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime
from netmiko import ConnectHandler
from my_devices import device_list


def ssh_conn(device):
    net_connect = ConnectHandler(**device)
    return net_connect.find_prompt()


if __name__ == "__main__":

    start_time = datetime.now()
    max_threads = 4

    pool = ProcessPoolExecutor(max_threads)
    future = pool.submit(ssh_conn, device_list[0])

    print(future.done())
    time.sleep(5)
    print(future.done())

    # Waits until the future is complete
    print("Result: " + future.result())

    end_time = datetime.now()
    print(end_time - start_time)
