# SuperFastPython.com
# example of shared semaphore using a manager
from time import sleep
from random import random
from multiprocessing import Manager
from multiprocessing import Pool

# custom function to be executed in a child process
def task(number, shared_semaphore):
    # acquire the shared semaphore
    with shared_semaphore:
        # generate a number between 0 and 1
        value = random()
        # block for a fraction of a second
        sleep(value)
        # report the generated value
        print(f'{number} got {value}')

# protect the entry point
if __name__ == '__main__':
    # create the manager
    with Manager() as manager:
        # create the shared semaphore
        managed_sem = manager.Semaphore(2)
        # create the shared pool
        with Pool() as pool:
            # prepare arguments for task
            args = [(i,managed_sem) for i in range(10)]
            # issue many tasks to the process pool
            pool.starmap(task, args)
