# SuperFastPython.com
# example of getting a list of active child processes
from time import sleep
from multiprocessing import active_children
from multiprocessing import Process

# custom function to be executed in a child process
def task():
    # block for a moment
    sleep(1)

# protect the entry point
if __name__ == '__main__':
    # create a number of child processes
    processes = [Process(target=task) for _ in range(5)]
    # start the child processes
    for process in processes:
        process.start()
    # get a list of all active child processes
    children = active_children()
    # report a count of active children
    print(f'Active Children Count: {len(children)}')
    # report each in turn
    for child in children:
        print(child)
