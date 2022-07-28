# SuperFastPython.com
# example of using an event object with processes
from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing import Event

# custom function to be executed in a child process
def task(shared_event, number):
    # wait for the event to be set
    print(f'Process {number} waiting...', flush=True)
    shared_event.wait()
    # begin processing, generate a random number
    value = random()
    # block for a fraction of a second
    sleep(value)
    # report a message
    print(f'Process {number} got {value}', flush=True)

# protect the entry point
if __name__ == '__main__':
    # create a shared event object
    event = Event()
    # create a suite of processes
    processes = [Process(target=task,
        args=(event, i)) for i in range(5)]
    # start all processes
    for process in processes:
        process.start()
    # block for a moment
    print('Main process blocking...')
    sleep(2)
    # trigger all child processes
    event.set()
    # wait for all child processes to terminate
    for process in processes:
        process.join()
