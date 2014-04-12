from multiprocessing import Process, Lock, Queue
import random, hashlib, time, os
import numpy
from numpy import random

def worker(queue,master_lock):
    while(1):
        #print 'Got into consumer method, with pid: %s' % os.getpid()
         master_lock.acquire()
         if queue.qsize() != 0:
            A = queue.get()
            #A=numpy.dot(A,A)
            print 'got msg: \n', A
         else:
            A = None
            print 'Queue looks empty'
         master_lock.release()
         #time.sleep(random.randrange(5,10))
def master(queue,worker_lock):
    while(1):
       #print 'Got into producer method, with pid: %s' % os.getpid()
       worker_lock.acquire()
       A=random.rand(2,2)       
       queue.put(A)
       print 'Produced msg: \n', A
       worker_lock.release()
       #time.sleep(random.randrange(5,10))

if __name__ == "__main__": 
    queue = Queue()
    master_lock = Lock()
    worker_lock = Lock()
    #l=len(os.listdir("/home/sarath/Desktop"))
    l=2
    master(queue,master_lock)
    worker(queue,worker_lock)
'''    while(1):
        if l !=0:
            for i in range(l):
                Process(target=master, args=(queue,worker_lock,)).start()
            l=l-1
        else:
            break
    time.sleep(1)
    while(1):
        if queue.qsize()!=0:
            for j in range(queue.qsize()):
                Process(target=worker, args=(queue,master_lock)).start()
        else:
            break'''
