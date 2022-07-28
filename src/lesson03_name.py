# SuperFastPython.com
# example of setting the process name in the constructor
from multiprocessing import Process

# protect the entry point
if __name__ == '__main__':
    # create a process with a custom name
    process = Process(name='MyProcess')
    # report process name
    print(process.name)
