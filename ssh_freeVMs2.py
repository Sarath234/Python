import subprocess
import numpy as np
import numpy as np
import scipy.io
from multiprocessing import Process, Lock, Queue
import random,time,pickle


def vmtimupdation():
    w=0
    while True:
        w+=1
        VM_per=[]
        freeVMs=[]
        ips=['192.168.32.217','192.168.32.218']
        for i in range(2):
            fil=str(i)+'.txt'
            f=open(fil,'r')
            VM_per.append(f.read())
            f.close()
#        print VM_per
        for i in range(len(VM_per)):
#            print VM_per[i]
            if float(VM_per[i])<40:
                freeVMs.append(ips[i])
        print freeVMs
        time.sleep(1)

'''def vmtimupdation():
    w=0
    while w<10:
        t=time.time()
        f=open('hosts','r')
        data=f.read()
        f.close()
#        print 'reading ',time.time()-t
        data=data.split('\n')
        #print len(data)
        #print data
        freeVMs=[]
        for i in range(len(data)-1):
            t2=time.time()
            per=(subprocess.check_output('ssh root@'+data[i]+' '+'nohup python /export/user/psutilexe.py',stdin=None,stderr=subprocess.STDOUT,shell=True)).split(' ')
            print 'sshing ', time.time()-t2
            #print 'CPU %=',float(per[0])
            #print 'MEM %=',float(per[1])
            if float(per[0])<90:
                freeVMs.append(data[i])
        #print freeVMs
        t1=time.time()
        fw=open('freeVMs','w')
        for i in freeVMs:
            fw.write('%s\n' %i)
        fw.close()
#        print 'writing ', time.time()-t1
        w=w+1
        print 'total ',time.time()-t

def worker(queue):
    while True:
        print 'before worker',queue1.qsize()
        if queue1.qsize()!=0:
            for j in range(queue1.qsize()):
                B=queue.get()
                f=open('hosts','r')
                data=f.read()
                f.close()
                data=data.split('\n')
                #print len(data)
                subprocess.call('mpiexec -f freeVMs -n'+' '+len(data)-1+' python mulpar_new.py',shell=True)                
        else:
            print 'Queue is Empty'
        time.sleep(5)

def jobcreat(queue,queue2):
    w=1
    job1=[]
    while w<21:

        data=pickle.load(open('job11.txt','rb'))
        for i in data:
            if queue.qsize()<10:
#                job.append(i)
#                print i
                i.append(time.time())
#                print i
                queue.put(i)
                time.sleep(5)
            else:
                time.sleep(20)'''


if __name__ == "__main__":
    Process(target=vmtimupdation).start()
#    Process(target=vmtimupdation).start()
#    Process(target=vmtimupdation).start()
