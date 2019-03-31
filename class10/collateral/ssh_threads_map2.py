from concurrent.futures import ThreadPoolExecutor
from my_devices import device_list
from netmiko import ConnectHandler
from datetime import datetime


def ssh_conn(device):
    return_dict = {}
    net_connect = ConnectHandler(**device)
    dns_name = net_connect.host
    my_prompt = net_connect.find_prompt()
    return_dict[dns_name] = my_prompt
    return return_dict


if __name__ == "__main__":

    start_time = datetime.now()
    max_threads = 4

    with ThreadPoolExecutor(max_threads) as pool:
        results_generator = pool.map(ssh_conn, device_list)

        # Results generator
        for result in results_generator:
            print(result)
            end_time = datetime.now()
            print(end_time - start_time)
