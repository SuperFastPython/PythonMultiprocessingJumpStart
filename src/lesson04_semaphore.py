# SuperFastPython.com
# example of a semaphore to limit access to resource
from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing import Semaphore

# custom function to be executed in a child process
def task(shared_semaphore, ident):
    # attempt to acquire the semaphore
    with shared_semaphore:
        # generate a random value between 0 and 1
        val = random()
        # block for a fraction of a second
        sleep(val)
        # report result
        print(f'Process {ident} got {val}', flush=True)

# protect the entry point
if __name__ == '__main__':
    # create the shared semaphore
    semaphore = Semaphore(2)
    # create processes
    processes = [Process(target=task,
        args=(semaphore, i)) for i in range(10)]
    # start child processes
    for process in processes:
        process.start()
    # wait for child processes to finish
    for process in processes:
        process.join()
