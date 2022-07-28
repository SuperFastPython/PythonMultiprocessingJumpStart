# SuperFastPython.com
# example of wait/notify with a condition for processes
from time import sleep
from multiprocessing import Process
from multiprocessing import Condition

# custom function to be executed in a child process
def task(shared_condition):
    # block for a moment
    sleep(1)
    # notify a waiting process that the work is done
    print('Child sending notification...', flush=True)
    with shared_condition:
        shared_condition.notify()

# protect the entry point
if __name__ == '__main__':
    # create a condition
    condition = Condition()
    # acquire the condition
    print('Main process waiting for data...')
    with condition:
        # create a new process to execute the task
        worker = Process(target=task, args=(condition,))
        # start the new child process
        worker.start()
        # wait to be notified by the child process
        condition.wait()
    # we know the data is ready
    print('Main process all done')
