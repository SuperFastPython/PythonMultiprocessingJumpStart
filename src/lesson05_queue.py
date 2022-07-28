# SuperFastPython.com
# example of producer and consumer processes with queue
from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing import Queue

# custom function for generating work (producer)
def producer(shared_queue):
    print('Producer: Running', flush=True)
    # generate work
    for _ in range(10):
        # generate a value
        value = random()
        # block
        sleep(value)
        # add to the queue
        shared_queue.put(value)
    # all done
    shared_queue.put(None)
    print('Producer: Done', flush=True)

# custom function for consuming work (consumer)
def consumer(shared_queue):
    print('Consumer: Running', flush=True)
    # consume work
    while True:
        # get a unit of work
        item = shared_queue.get()
        # check for stop
        if item is None:
            break
        # report
        print(f'>got {item}', flush=True)
    # all done
    print('Consumer: Done', flush=True)

# protect the entry point
if __name__ == '__main__':
    # create the shared queue
    queue = Queue()
    # start the consumer
    consumer_p = Process(target=consumer, args=(queue,))
    consumer_p.start()
    # start the producer
    producer_p = Process(target=producer, args=(queue,))
    producer_p.start()
    # wait for all processes to finish
    producer_p.join()
    consumer_p.join()
