#!/usr/bin/env python
from __future__ import print_function
from multiprocessing import Process, Queue
import random


def my_func(name, output_q):
    output_dict = {}
    output_dict[name] = []
    for i in range(0, 50000):
        # print(i)
        # print(output_q.full())
        output_dict[name].append(random.getrandbits(128))

    output_q.put(output_dict)
    return


def main():
    test_list = ["test1", "test2", "test3"]
    output_q = Queue()
    procs = []
    gatherstruct = []

    for entry in test_list:
        my_proc = Process(target=my_func, args=(entry, output_q))
        my_proc.start()
        procs.append(my_proc)

    while True:
        # True if any process is still running
        still_running = any(a_proc.is_alive() for a_proc in procs)
        while not output_q.empty():
            gatherstruct.append(output_q.get())
        if not still_running:
            break

    while not output_q.empty():
        gatherstruct.append(output_q.get())

    print(gatherstruct)


if __name__ == "__main__":
    main()
