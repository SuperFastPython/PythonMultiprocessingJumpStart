# SuperFastPython.com
# example of using a pipe between processes
from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing import Pipe

# custom function generate work items (sender)
def sender(connection):
    print('Sender: Running', flush=True)
    # generate work
    for _ in range(10):
        # generate a value
        value = random()
        # block
        sleep(value)
        # send data
        connection.send(value)
    # all done, signal to expect no further messages
    connection.send(None)
    print('Sender: Done', flush=True)

# custom function to consume work items (receiver)
def receiver(connection):
    print('Receiver: Running', flush=True)
    # consume work
    while True:
        # get a unit of work
        item = connection.recv()
        # report
        print(f'>receiver got {item}', flush=True)
        # check for stop
        if item is None:
            break
    # all done
    print('Receiver: Done', flush=True)

# protect the entry point
if __name__ == '__main__':
    # create the pipe
    conn1, conn2 = Pipe()
    # start the sender
    sender_p = Process(target=sender, args=(conn2,))
    sender_p.start()
    # start the receiver
    receiver_p = Process(target=receiver, args=(conn1,))
    receiver_p.start()
    # wait for all processes to finish
    sender_p.join()
    receiver_p.join()
