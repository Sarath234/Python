from multiprocessing import Process, Lock, Queue
from apscheduler.scheduler import Scheduler
from numpy import *
import subprocess
import math
import pwd
import grp
import os,time
import numpy as np

def worker(queue,master_lock):
    master_lock.acquire()
    #print 'before worker',queue.qsize()
    queue.get()
    subprocess.call('mpiexec -n 1 python mulpar1.py &',shell=True)
    master_lock.release()

def masterslave(queue,worker_lock):
    worker_lock.acquire()
    uid=pwd.getpwnam('nobody').pw_uid
    gid=grp.getgrnam('nogroup').gr_gid
    A=np.random.uniform(size=(2,2)).astype('d')
    savetxt('mat.txt',A,delimiter=',',fmt='%3.3f')
    #print A
    os.chown('mat.txt',uid,gid)
    queue.put(1)
    worker_lock.release()

def master(queue,worker_lock):
    sched=Scheduler()
    sched.start()
    sched.add_cron_job(lambda: masterslave(queue,worker_lock), second='*/1')
    time.sleep(1)

if __name__ == "__main__": 
    queue = Queue()
    master_lock = Lock()
    worker_lock = Lock()
    
    while True:
        t1=time.time()
        Process(target=master,args=(queue,worker_lock)).start()
        print time.time()-t1
        if queue.qsize()!=0:            
            for j in range(queue.qsize()):
                Process(target=worker, args=(queue,master_lock)).start()
        else:
            #print 'Queue is Empty'
            time.sleep(1)
