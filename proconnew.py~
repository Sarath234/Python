from multiprocessing import Process, Lock, Queue
from apscheduler.scheduler import Scheduler
from numpy import *
import subprocess
import math
import pwd
import grp
import os,time
import numpy as np

def worker(queue,queue1):
    while True:
        print 'before worker',queue1.qsize()
        if queue.qsize()!=0:
            for j in range(queue.qsize()):
                
                B=queue.get()
                queue1.get()
                subprocess.call('mpiexec -n 1 python mulpar1.py '+B+'&', shell=True)
        else:
            print 'Queue is Empty'
            time.sleep(0.1)

def masterslave(queue,queue1):
    j=0
    while True:
        uid=pwd.getpwnam('nobody').pw_uid
        gid=grp.getgrnam('nogroup').gr_gid
        A=random.rand(2000,2000).astype('d')
        print A
        savetxt('mat'+str(j)+'.txt',A,delimiter=',',fmt='%3.3f')
        A=None
        os.chown('mat.txt',uid,gid)
        queue.put('mat'+str(j)+'.txt')
        queue1.put(1)
        j=j+1
        time.sleep(1)

if __name__ == "__main__": 
    queue = Queue()
    queue1 = Queue()
    Process(target=masterslave,args=(queue,queue1,)).start()
    Process(target=worker, args=(queue,queue1,)).start()
'''    if queue1.qsize()!=0:
        print 'before worker',queue1.qsize()
        Process(target=worker, args=(queue,queue1,)).start()
    else:
        print 'Queue is Empty'
        time.sleep(0.1)'''
