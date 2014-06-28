import subprocess
import numpy as np
import scipy.io
from multiprocessing import Process, Lock, Queue,Value,Array,Manager
import random,time,pickle,os

mat=scipy.io.loadmat('simulationdata.mat')
b=mat['simulationdata']
mat=None
x=b[:,0]
y=b[:,1]
z=b[:,2]
x=x.reshape(60,1)
y=y.reshape(60,1)
z=z.reshape(60,1)

def read_cpu(fil):
    f=open(fil,'r')
    cpu_per=f.read()
    f.close()
    try:
        return float(cpu_per)
    except:
        read_cpu(fil)


def free_vms_update():
    VM_per=[]
    freeVMs=[]
    ips=['192.168.122.245','192.168.122.148','192.168.122.195','192.168.122.65']#,'192.168.122.34','192.168.122.35','192.168.122.128','192.168.122.232','192.168.122.39','192.168.122.191']
    for i in range(4):
        fil=str(i)+'.txt'
        VM_per.append(read_cpu(fil))
    for i in range(len(VM_per)):
        if VM_per[i]<60:
            freeVMs.append(ips[i])
    return freeVMs



def vmtimupdation():
    while True:
        freeVMs=free_vms_update()
        d=len(freeVMs)
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

def vm1(s,argmt,freeVMs):
#    print 's',s
#    print 'argmt',argmt
#    print 'freeVMs',freeVMs

    for i in range(0,len(s)):
        fil_nam_freeVMs='freeVMs'+str(i)+'.txt'
        fw=open(fil_nam_freeVMs,'w')
#        vm01='192.168.122.142'
#        fw.write('%s\n' %vm01)
        for j in range(0,argmt[i]):
<<<<<<< HEAD
            if i==0:
                print 'freeVMs writing',freeVMs[j]
                fw.write('%s\n' %freeVMs[j])
            else:
                print 'freeVMs writing',freeVMs[j+argmt[i-1]]
                fw.write('%s\n' %freeVMs[j+argmt[i-1]])
        fw.close()
#        time.sleep(1)
#        print 'mpiexec -f '+fil_nam_freeVMs+' -n'+' '+str(argmt[i])+' python mulpar_new.py '+s[i]

        subprocess.call('ssh root@'+freeVMs[]mpiexec -f '+fil_nam_freeVMs+' -n'+' '+str(argmt[i]+1)+' python mulpar_new.py '+s[i]+' &',shell=True)
#        os.remove(fil_nam_freeVMs)
=======
            print 'freeVMs writing',freeVMs[j]
            fw.write('%s\n' %freeVMs[j])
            fw.close()
#        print 'mpiexec -f '+fil_nam_freeVMs+' -n'+' '+str(argmt[i])+' python mulpar_new.py '+s[i]
        subprocess.call('mpiexec -f '+fil_nam_freeVMs+' -n'+' '+str(argmt[i])+' python mulpar_new.py '+s[i]+' &',shell=True)
        os.remove(fil_nam_freeVMs)
>>>>>>> 52ef1af4f2045228569fc363ab7a99c45352687e


def worker(queue):
    delay=[]
    while True:
        if queue.qsize()!=0:
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
#            print s,'\n',dt,'\n',tim
            freeVMs=free_vms_update()
            no_of_freeVMs=len(freeVMs)
            while no_of_freeVMs<len(s):
                req_vms=len(s)-no_of_freeVMs
#                print 'no of free vms ', no_of_freeVMs
#                print 'lenght of jobs ', len(s)
#                print 'required vms ', req_vms
                while req_vms>0:
#                    print 'no_of_freeVMs=',no_of_freeVMs
                    time.sleep(1)
                    freeVMs=free_vms_update()
                    no_of_freeVMs=len(freeVMs)
                    req_vms=req_vms-no_of_freeVMs
            freeVMs=free_vms_update()
            no_of_freeVMs=len(freeVMs)
            C= mat_creat(s,dt,no_of_freeVMs)
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
#            print 'argmnt', argmt
            freeVMs=free_vms_update()
            no_of_freeVMs=len(freeVMs)
            
            if y<=no_of_freeVMs:
                vm1(s,argmt,freeVMs)
############################################ if vm1 didn't work use below#########################################
#                for i in range(0,len(s)):
#                    fil_nam_freeVMs='freeVMs'+str(i)+'.txt'
#                    fw=open(fil_nam_freeVMs,'w')
#                    for j in range(0,argmt[i]):
#                        print 'freeVMs writing',freeVMs[j]
#                        fw.write('%s\n' %freeVMs[j])
#                    fw.close()
#                    print 'mpiexec -f '+fil_nam_freeVMs+' -n'+' '+str(argmt[i])+' python mulpar_new.py '+s[i]
#                    subprocess.call('mpiexec -f '+fil_nam_freeVMs+' -n'+' '+str(argmt[i])+' python mulpar_new.py '+s[i],shell=True)
#                    os.remove(fil_nam_freeVMs)
            else:
                extra_delay=[]
                j_lis=[]
                freeVMs=free_vms_update()
                no_of_freeVMs=len(freeVMs)
                excess=y-no_of_freeVMs
                temp=[]
                min_=[0]*len(argmt)
                truth_value=True
                for i in range(0,len(argmt)):
                    if argmt[i]==1:
                        temp.append(i)
                        min_[i]=0
                    else:
                        min_[i]=C[i,argmt[i]-2]-C[i,argmt[i]-1]

                if len(temp)==len(argmt):
                    truth_value=False
                for i in range(0,len(argmt)):
                    xtemp=min_[i]-minv[i]
                    extra_delay.append(xtemp)
                max1=np.max(extra_delay)+1
                for i in range(0,len(temp)):
                    extra_delay[temp[i]]=max1

                while excess>0 and truth_value==True:
                    I=np.argmin(extra_delay)
                    if argmt[I] !=1:
                       argmt[I]=argmt[I]-1
                       extra_delay[I]=C[I,argmt[I]-2]-C[I,argmt[I]-1]
                       excess=excess-1
                    else:
                       max2=np.max(extra_delay)+1
                       extra_delay[I]=max2
                    truth=0
                    for i in range(0,len(argmt)):
                       truth=truth+argmt[i]
                    if truth==len(argmt):
                       truth_value=False

                freeVMs=free_vms_update()
                vm1(s,argmt,freeVMs)

def jobcreat(queue):
    for i in range(2):
        print 'queue size IN JOB CREATE',queue.qsize() 
        fil_name=str(11+i)+'.txt'
        f=open(fil_name,'r')
        data=f.read().split(',')
        f.close()
#        print data
        data.append(time.time())
        queue.put(data)
        time.sleep(5)
<<<<<<< HEAD
=======
#        else:
#            time.sleep(20)
>>>>>>> 52ef1af4f2045228569fc363ab7a99c45352687e

if __name__ == "__main__":
    manage=Manager()
#    d=Value('d',0.0)
#    arr=Array('s')
    queue = Queue()
    Process(target=vmtimupdation,args=()).start()
    Process(target=worker,args=(queue,)).start()
    Process(target=jobcreat,args=(queue,)).start()
