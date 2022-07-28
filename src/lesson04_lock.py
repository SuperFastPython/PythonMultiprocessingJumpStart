# SuperFastPython.com
# example of protecting a critical section with a mutex
from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing import Lock

# custom function to be executed in a child process
def task(shared_lock, ident, value):
    # acquire the lock
    with shared_lock:
        # report a message
        print(f'>{ident} got lock, sleeping {value}',
            flush=True)
        # block for a fraction of a second
        sleep(value)

# protect the entry point
if __name__ == '__main__':
    # create the shared mutex lock
    lock = Lock()
    # create a number of processes with different args
    processes = [Process(target=task,
        args=(lock, i, random())) for i in range(10)]
    # start the processes
    for process in processes:
        process.start()
    # wait for all processes to finish
    for process in processes:
        process.join()
