# SuperFastPython.com
# example of shared ctype accessed in multiple processes
from random import random
from multiprocessing import Value
from multiprocessing import Process

# custom function to be executed in a child process
def task(shared_var):
    # generate a single floating point value
    generated = random()
    # store value
    shared_var.value = generated
    # report progress
    print(f'Wrote: {shared_var.value}', flush=True)

# protect the entry point
if __name__ == '__main__':
    # create shared variable
    variable = Value('f', 0.0)
    # create a child process process
    process = Process(target=task, args=(variable,))
    # start the process
    process.start()
    # wait for the process to finish
    process.join()
    # read the value
    data = variable.value
    # report the value
    print(f'Read: {data}')
