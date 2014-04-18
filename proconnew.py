from multiprocessing import Process, Lock, Queue
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
        if queue1.qsize()!=0:
            for j in range(queue1.qsize()):
                B=queue.get()
                queue1.get()
                subprocess.call('mpiexec -n 1 python mulpar.py '+B+'&', shell=True)
                
        else:
            print 'Queue is Empty'
        time.sleep(5)

def master(queue,queue1):
    j=0
    while True:
        uid=pwd.getpwnam('nobody').pw_uid
        gid=grp.getgrnam('nogroup').gr_gid
        matrix_size=[105,1000,225,400,200]
        l=matrix_size[random.randint(1)]
        A=random.rand(l,l).astype('d')
        savetxt('mat'+str(j)+'.txt',A,delimiter=',',fmt='%3.3f')
        A=None
        os.chown('mat'+str(j)+'.txt',uid,gid)
        queue.put('mat'+str(j)+'.txt')
        queue1.put(1)
        j=j+1
        time.sleep(1)
       
if __name__ == "__main__": 
    queue = Queue()
    queue1 = Queue()
    Process(target=master,args=(queue,queue1,)).start()
    Process(target=worker, args=(queue,queue1,)).start()
