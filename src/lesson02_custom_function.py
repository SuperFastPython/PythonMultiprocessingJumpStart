# SuperFastPython.com
# example of running a function in a new child process
from time import sleep
from multiprocessing import Process

# custom function to be executed in a child process
def task():
    # block for a moment
    sleep(1)
    # report a message
    print('This is from another process', flush=True)

# protect the entry point
if __name__ == '__main__':
    # create a new process instance
    process = Process(target=task)
    # start executing the function in the process
    process.start()
    # wait for the process to finish
    print('Waiting for the process...')
    process.join()
