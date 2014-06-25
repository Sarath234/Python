from multiprocessing import Process, Lock, Queue
from numpy import *
import subprocess
import math
import pwd
import grp
import os,time
import numpy as np

'''def worker(queue,queue1):
    while True:
        print 'before worker',queue1.qsize()
        if queue1.qsize()!=0:
            for j in range(queue1.qsize()):
                B=queue.get()
                queue1.get()
                subprocess.call('mpiexec -f hosts -n 4 python mulpar1.py '+B+'&', shell=True)                
        else:
            print 'Queue is Empty'
        time.sleep(5)'''

def master(queue,queue1):
    j=0
    while True:
        uid=pwd.getpwnam('nobody').pw_uid
        gid=grp.getgrnam('nogroup').gr_gid
        matrix_size=[2000,2500]
        l=matrix_size[random.randint(1)]
        A=random.rand(l,l).astype('d')
        savetxt('mat'+str(j)+'.txt',A,delimiter=',',fmt='%3.3f')
        A=None
        os.chown('mat'+str(j)+'.txt',uid,gid)
        queue.put('mat'+str(j)+'.txt')
        queue1.put(1)
        j=j+1
        print j
#        per=(subprocess.check_output('ssh root@192.168.32.218 nohup python /export/user/psutilexe.py',stdin=None,stderr=subprocess.STDOUT,shell=True)).split(' ')
#        print 'CPU %=',float(per[0])
#        print 'MEM %=',float(per[1])
        time.sleep(2)
       
if __name__ == "__main__": 
    queue = Queue()
    queue1 = Queue()
    Process(target=master,args=(queue,queue1,)).start()
#    Process(target=worker, args=(queue,queue1,)).start()
