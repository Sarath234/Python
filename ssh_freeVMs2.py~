import subprocess
import numpy as np
import scipy.io
from multiprocessing import Process, Lock, Queue,Value
import random,time,pickle

def vmtimupdation(d):
    w=0
    while True:
#        t=time.time()
        w+=1
        VM_per=[]
        freeVMs=[]
        ips=['192.168.32.218','192.168.32.217']
        for i in range(2):
            fil=str(i)+'.txt'
            f=open(fil,'r')
            VM_per.append(f.read())
            f.close()
#        print VM_per
        for i in range(len(VM_per)):
#            print VM_per[i]
            try: 
                VM_p=float(VM_per[i])
                if VM_p<40:
                    freeVMs.append(ips[i])
            except:
                pass
        d.value=len(freeVMs)
        print freeVMs
#        print time.time()-t
        time.sleep(1)

def worker(d,queue):
    while True:
#        print 'No of Free VMs',d.value
#        w+=1
        if queue.qsize()!=0:
#            vms=queue2.get()
            quejob=queue.get()
            i = (len(quejob)-1)/2
            s = []
  	    dt = []
            tim=quejob[-1]
            while (i>0):
                s.append(quejob[2*i-2])
                dt.append(int(quejob[2*i-1]))
                i = i - 1
            s=s[::-1]
            dt=dt[::-1]
            print s,'\n',dt,'\n',tim
            time.sleep(5)

        else:
            print 'Queue is Empty'''
            time.sleep(5)


def jobcreat(queue):
    for i in range(20):
        if queue.qsize()<10:
            fil_name=str(11+i)+'.txt'
            f=open(fil_name,'r')
            data=f.read().split(',')
            f.close()
            print data
            data.append(time.time())
            queue.put(data)
            time.sleep(5)
        else:
            time.sleep(20)

if __name__ == "__main__":
    d=Value('d',0.0)
    queue = Queue()
    Process(target=vmtimupdation,args=(d,)).start()
    Process(target=worker,args=(d,queue)).start()
    Process(target=jobcreat,args=(queue,)).start()
