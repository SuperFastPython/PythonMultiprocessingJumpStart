# SuperFastPython.com
# example of sharing global between forked processes
from multiprocessing import Process
from multiprocessing import set_start_method

# custom function to be executed in a child process
def task():
    # declare global state
    global data
    # report global state
    print(f'child process before: {data}', flush=True)
    # change global state
    data = 'hello hello!'
    # report global state
    print(f'child process after: {data}', flush=True)

# protect the entry point
if __name__ == '__main__':
    # set the start method to fork
    set_start_method('fork')
    # define global state
    data = 'Hello there'
    # report global state
    print(f'main process: {data}')
    # start a child process
    process = Process(target=task)
    process.start()
    # wait for the child to terminate
    process.join()
    # report global state
    print(f'main process: {data}')
