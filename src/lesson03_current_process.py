# SuperFastPython.com
# example of getting access to the current process
from multiprocessing import current_process

# protect the entry point
if __name__ == '__main__':
    # get the current process
    process = current_process()
    # report details
    print(process)
