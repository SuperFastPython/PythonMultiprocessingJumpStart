# SuperFastPython.com
# example of executing an async one-off task
from multiprocessing import Pool

# custom function to be executed in a child process
def task():
    # report a message
    print('This is another process', flush=True)

# protect the entry point
if __name__ == '__main__':
    # create the multiprocessing pool
    with Pool() as pool:
        # issue a task asynchronously
        async_result = pool.apply_async(task)
        # wait for the task to complete
        async_result.wait()
