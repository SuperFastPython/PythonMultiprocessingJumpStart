# SuperFastPython.com
# example of reporting the native process identifier
from multiprocessing import Process

# protect the entry point
if __name__ == '__main__':
    # create the process
    process = Process()
    # report the process identifier
    print(process.pid)
    # start the process
    process.start()
    # report the process identifier
    print(process.pid)
