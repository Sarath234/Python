import subprocess
import time
from numpy import *
import math
import pwd
import grp
import os
import numpy as np

comtim=[]

def creatmat(i):
    uid=pwd.getpwnam('nobody').pw_uid
    gid=grp.getgrnam('nogroup').gr_gid
    A=np.random.uniform(size=(i,i)).astype('d')
    savetxt('mat.txt',A,delimiter=',',fmt='%3.3f')
    os.chown('mat.txt',uid,gid)

def my_range(start,end,step):
    while start<=end:
        yield start
        start+=step

def test1():
    print '1 VM'
    t1=time.time()
    subprocess.call('mpiexec -f hosts1 -n 2 python mulpar_new.py',shell=True)
    comtim.append(time.time()-t1)
    print time.time()-t1
    time.sleep(0.1)

    print '2 VMs'
    t2=time.time()
    subprocess.call('mpiexec -f hosts2 -n 3 python mulpar_new.py',shell=True)
    comtim.append(time.time()-t2)
    print time.time()-t2
    time.sleep(0.1)

    print '3 VM'
    t3=time.time()
    subprocess.call('mpiexec -f hosts3 -n 4 python mulpar_new.py',shell=True)
    comtim.append(time.time()-t3)
    print time.time()-t3
    time.sleep(0.1)

    print '4 VMs'
    t4=time.time()
    subprocess.call('mpiexec -f hosts4 -n 5 python mulpar_new.py',shell=True)
    comtim.append(time.time()-t4)
    print time.time()-t4
    time.sleep(0.1)

    print '5 VM'
    t5=time.time()
    subprocess.call('mpiexec -f hosts5 -n 6 python mulpar_new.py',shell=True)
    comtim.append(time.time()-t5)
    print time.time()-t5
    time.sleep(0.1)

    print '6 VMs'
    t6=time.time()
    subprocess.call('mpiexec -f hosts6 -n 7 python mulpar_new.py',shell=True)
    comtim.append(time.time()-t6)
    print time.time()-t6
    time.sleep(0.1)

    print '7 VM'
    t7=time.time()
    subprocess.call('mpiexec -f hosts7 -n 8 python mulpar_new.py',shell=True)
    comtim.append(time.time()-t7)
    print time.time()-t7
    time.sleep(0.1)

    print '8 VMs'
    t8=time.time()
    subprocess.call('mpiexec -f hosts8 -n 9 python mulpar_new.py',shell=True)
    comtim.append(time.time()-t8)
    print time.time()-t8
    time.sleep(0.1)

    print '9 VM'
    t9=time.time()
    subprocess.call('mpiexec -f hosts9 -n 10 python mulpar_new.py',shell=True)
    comtim.append(time.time()-t9)
    print time.time()-t9
    time.sleep(0.1)

    print '10 VMs'
    t10=time.time()
    subprocess.call('mpiexec -f hosts10 -n 11 python mulpar_new.py',shell=True)
    comtim.append(time.time()-t10)
    print time.time()-t10
    time.sleep(0.1)

for l in my_range(1000,3000,50):
    creatmat(l)
    test1()

savetxt('comtim.txt',comtim,fmt='%3.3f')
