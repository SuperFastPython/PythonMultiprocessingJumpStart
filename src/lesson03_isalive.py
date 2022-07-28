# SuperFastPython.com
# example of assessing whether a process is alive
from multiprocessing import Process

# protect the entry point
if __name__ == '__main__':
    # create the process
    process = Process()
    # report the process is alive
    print(process.is_alive())
