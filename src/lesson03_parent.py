# SuperFastPython.com
# example of getting the parent process
from multiprocessing import parent_process

# protect the entry point
if __name__ == '__main__':
    # get the parent process
    process = parent_process()
    # report details
    print(process)
