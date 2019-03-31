from concurrent.futures import ProcessPoolExecutor, wait
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

    future_list = []
    for a_device in device_list:
        future = pool.submit(ssh_conn, a_device)
        future_list.append(future)

    # Waits until all the pending threads are done
    wait(future_list)

    for future in future_list:
        print("Result: " + future.result())

    end_time = datetime.now()
    print(end_time - start_time)
