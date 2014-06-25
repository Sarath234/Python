import subprocess
import numpy as np
import scipy.io
from multiprocessing import Process, Lock, Queue,Value,Array,Manager
import random,time,pickle,os

#mat=scipy.io.loadmat('simulationdata.mat')
#b=mat['simulationdata']
#mat=None
#x=b[:,0]
#y=b[:,1]
#z=b[:,2]
#x=x.reshape(60,1)
#y=y.reshape(60,1)
#z=z.reshape(60,1)

def read_cpu(fil):
    f=open(fil,'r')
    cpu_per=f.read()
    f.close()
    try:
        return float(cpu_per)
    except:
        read_cpu(fil)


def vmtimupdation(d):
    while True:
#        t=time.time()
        VM_per=[]
        freeVMs=[]
        ips=['192.168.122.245','192.168.122.148','192.168.122.195','192.168.122.65','192.168.122.34','192.168.122.35','192.168.122.128','192.168.122.232','192.168.122.39','192.168.122.191']
        for i in range(5):
            fil=str(i)+'.txt'
            VM_per.append(read_cpu(fil))
        for i in range(len(VM_per)):
            if VM_per[i]<60:
                freeVMs.append(ips[i])
        d.value=len(freeVMs)
        print 'VMUpdation process= ',freeVMs
        print 'VMs=',len(freeVMs)
        time.sleep(1)

def find_tim(a,b):
    c=len(np.loadtxt(a,delimiter=','))
    for i in range(0,len(x[:,0])):
        if c==x[i,0]:
            if b==y[i,0]:
#                print 'time z=', z[i,0]
                return z[i,0]


def mat_creat(s,dt,free_vms):
#    print s
#    print dt
#    print free_vms
#    A=np.zeros(shape=(len(s),free_vms))
#    print A
#    return A
    A=np.zeros(shape=(len(s),free_vms))
    j=1
    for i in range(0,int(free_vms)):
        for k in range(0,len(s)):
#            print s[k]
#            print find_tim(s[k],j)
            ab=find_tim(s[k],j)-dt[k]
            if(ab>0):
                A[k,i]=ab
            else:
                A[k,i]=0
        j=j+1
    return A

def worker(d,queue):
    while True:
#        print 'No of Free VMs',d.value
#        w+=1
#        print 'queue size',queue.qsize() 
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
 #           print s,'\n',dt,'\n',tim
            while d.value<len(s):
                freVMs=d.value
                req_vms=len(s)-freVMs
#                print 'free vms ', freVMs
#                print 'lenght of jobs ', len(s)
#                print 'required vms ', req_vms
                while req_vms>0:
#                    print 'd value= ',d.value
                    time.sleep(1)
                    frvm=d.value
#                    print 'free vms = ', frvm
                    req_vms=req_vms-frvm
            
            C= mat_creat(s,dt,d.value)
#            print 'C matrix= \n', C
            y=0
            argmt=[]
            minv=[]
            for l in range(0,C.shape[0]):
                argmt.append(np.argmin(C[l,:])+1)
                minv.append(np.min(C[l,:]))
                y=y+argmt[l]
#            print 'minv= ',minv
#            print 'y', y
#            print 'd', d.value
#            print 'argmnt', argmt
            
            if y<=d.value:
                VM_per=[]
                freeVMs=[]
                ips=['192.168.122.245','192.168.122.148','192.168.122.195','192.168.122.65','192.168.122.34','192.168.122.35','192.168.122.128','192.168.122.232','192.168.122.39','192.168.122.191']
                for i in range(5):
                    fil=str(i)+'.txt'
                    VM_per.append(read_cpu(fil))

                for i in range(len(VM_per)):
                    if VM_p<20:
                        freeVMs.append(ips[i])
#                print 'worker procee=',freeVMs

                for i in range(0,len(s)):
                    fil_nam_freeVMs='freeVMs'+str(i)+'.txt'
                    fw=open(fil_nam_freeVMs,'w')
                    for j in range(0,argmt[i]):
                        print 'freeVMs writing',freeVMs[j]
                        fw.write('%s\n' %freeVMs[j])
                    fw.close()
                    #print 'mpiexec -f '+fil_nam_freeVMs+' -n'+' '+str(argmt[i])+' python mulpar_new.py '+s[i]
                    subprocess.call('mpiexec -f '+fil_nam_freeVMs+' -n'+' '+str(argmt[i])+' python mulpar_new.py '+s[i],shell=True)
                time.sleep(5)

        else:
            print 'Queue is Empty'
            time.sleep(5)

def jobcreat(queue):
    for i in range(20):
        print 'queue size IN JOB CREATE',queue.qsize() 
        if queue.qsize()<10:
            fil_name=str(11+i)+'.txt'
            f=open(fil_name,'r')
            data=f.read().split(',')
            f.close()
#            print data
            data.append(time.time())
            queue.put(data)
            time.sleep(5)
        else:
            time.sleep(20)

if __name__ == "__main__":
    manage=Manager()
    d=Value('d',0.0)
#    arr=Array('s')
    queue = Queue()
    Process(target=vmtimupdation,args=(d,)).start()
#    Process(target=worker,args=(d,queue,)).start()
#    Process(target=jobcreat,args=(queue,)).start()
