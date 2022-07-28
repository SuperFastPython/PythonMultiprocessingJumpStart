# SuperFastPython.com
# example of checking the exit status of a child process
from time import sleep
from multiprocessing import Process

# custom function to be executed in a child process
def task():
    # block for a moment
    sleep(1)

# protect the entry point
if __name__ == '__main__':
    # create the process
    process = Process(target=task)
    # report the exit status
    print(process.exitcode)
    # start the process
    process.start()
    # report the exit status
    print(process.exitcode)
    # wait for the process to finish
    process.join()
    # report the exit status
    print(process.exitcode)
