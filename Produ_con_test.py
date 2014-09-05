from multiprocessing import Queue
import numpy,time
from numpy import random
from apscheduler.scheduler import Scheduler

def worker(queue):
    A = queue.get()
    print 'got msg: \n', numpy.dot(A,A)
    
def master(queue):
    A=random.rand(2,2)       
    queue.put(A)
    print 'Produced msg: \n', A
    
if __name__ == "__main__": 
    queue = Queue()
    sched=Scheduler()
    sched.start()
    sched.add_cron_job(lambda: master(queue), second='*/1')
    while True:
        time.sleep(1)
        if queue.qsize()!=0:
            for j in range(queue.qsize()):
                worker(queue)
        else:
            break

