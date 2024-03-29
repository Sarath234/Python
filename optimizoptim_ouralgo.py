import numpy as np
import scipy.io
from multiprocessing import Process, Lock, Queue
import random,time

mat=scipy.io.loadmat('simulationdata.mat')
b=mat['simulationdata']
mat=None
x=b[:,0]
y=b[:,1]
z=b[:,2]
x=x.reshape(60,1)
y=y.reshape(60,1)
z=z.reshape(60,1)

vms=[0]*5

def vm1(vms,argmt,minv):
    vm=[]
    vms=sorted(vms)
#    print vms
#    print argmt
#    print minv
    for i in range(0,len(argmt)):
#        print argmt[i]
        for j in range(0,argmt[i]):
            vm.append(minv[i])
#    print 'vm1 function,= ',vm
#    print vms
    for i in range(0,len(vm)):
        vms[i]=vm[i]
    
    return vms

def find_tim(a,b):
    for i in range(0,len(x[:,0])):
        if a==x[i,0]:
            if b==y[i,0]:
#                print z[i,0]
                return z[i,0]

def mat_creat(s,dt,free_vms):
#    print vms
#    vms=queue2.get()
#    queue2.put(vms)
#    print len(vms)
    A=np.zeros(shape=(len(s),free_vms))
    j=1
    for i in range(0,free_vms):
        for k in range(0,len(s)):
#           print find_tim(s[k],j)
            ab=find_tim(s[k],j)-dt[k]
            if(ab>0):
                A[k,i]=ab
            else:
                A[k,i]=0
        j=j+1
    return A

def optialgo(queue,queue2):
    w=0
    delay2=[]
    while w<30:
        w+=1
        if queue.qsize()!=0:
            vms=queue2.get()
            quejob=queue.get()
            i = (len(quejob)-1)/2
            s = []
  	    dt = []
            tim=quejob[-1]
            while (i>0):
                s.append(quejob[2*i-2])
                dt.append(quejob[2*i-1])
                i = i - 1
            s=s[::-1]
            dt=dt[::-1]
#            print s,'\n',dt,'\n',tim
            K=vms.count(0.0)
            queue2.put(vms)

            while vms.count(0)<len(s):
                vms=queue2.get()
                freVMs=vms.count(0)
                Ln_vms=len(vms)
                req_vms=len(s)-freVMs
#                print 'free vms ', freVMs
#                print 'lenght of jobs ', len(s)
#                print 'required vms ', len(s)-freVMs
                if Ln_vms<10:
                    if Ln_vms==9 and req_vms==2:
                        vms.append(0)
                        queue2.put(vms)
                    else:
                        for i in range(0,req_vms):
                            vms.append(0)
                        queue2.put(vms)
                else:
                    queue2.put(vms)
                    while req_vms>0:
                        time.sleep(np.min(vms))
                        vms=queue2.get()
                        frvm=vms.count(0)
                        queue2.put(vms)
#                        print 'Im Working'
                        req_vms=req_vms-frvm

            vms=queue2.get()
            N=vms.count(0)
            A= mat_creat(s,dt,N)
#            print 'A= ',A
#            print vms
#            queue2.put(vms)
            y=0
            delay=0
            argmt=[]
            minv=[]
            for l in range(0,A.shape[0]):
                argmt.append(np.argmin(A[l,:])+1)
                minv.append(np.min(A[l,:]))
                y=y+argmt[l]
                delay=delay+np.min(A[l,:])
#            print 'minv= ',minv
            if y<=N:
#                print argmt
#                print minv
                minvv=[]
                for i in range(0,len(s)):
                    minvv.append(find_tim(s[i],argmt[i]))

                vms=vm1(vms,argmt,minvv)
#                print 'if',vms
                queue2.put(vms)
                print "Delay in if= ",time.time()-tim
                delay2.append(time.time()-tim)
                time.sleep(5)

            else:
                extradelay=[]
                J_lis=[]
                N=vms.count(0)
#                print "VMs are free= ", N
                excess=y-N
#                print excess
                temp=[]
                min_=[0]*len(argmt)
                truth_value=True
                for n in range(0,len(argmt)):
                    if argmt[n]==1:
                        temp.append(n)
                        min_[n]=0
                    else:
#                        print 'argment= ',argmt
                        min_[n]=A[n,argmt[n]-2]-A[n,argmt[n]-1]

                if len(temp)==len(argmt):
                    truth_value=False
#                print 'argment= ',argmt
#                print 'min_= ',min_
#                print 'minv= ',minv
                for m in range(0,len(argmt)):
                    xtemp=min_[m]-minv[m]
                    extradelay.append(xtemp)
                max1= np.max(extradelay)+1
                for m in range(0,len(temp)):
                    extradelay[temp[m]]=max1
#                print extradelay
                while excess>0 and truth_value==True:
                    I=np.argmin(extradelay)
                    argmt[I]=argmt[I]-1
                    extradelay[I]=A[I,argmt[I]-2]-A[I,argmt[I]-1]
                    excess=excess-1
                    truth=0
                    for m in range(0,len(argmt)):
                        truth=truth+argmt[m]
                    if truth==len(argmt):
                        truth_value=False 
#                print 'extradelay list', extradelay

                minvv=[]
#                print argmt
#                print s
                for i in range(0,len(argmt)):
#                    print argmt[i]
#                    print s[i]
                    minvv.append(find_tim(s[i],argmt[i]+1))
                vms=vm1(vms,argmt,minvv)
                queue2.put(vms)
#                print dt
#                print minvv
                delay=0
                for i in range(0,len(s)):
                    xyz=minvv[i]-dt[i]
                    if xyz>=0:
                        delay=delay+minvv[i]-dt[i]
                    else:
                        delay=delay

                print 'delay New= ',delay+time.time()-tim
                delay2.append(time.time()-tim+delay)

                time.sleep(5)
        else:
            print 'Queue is Empty'
            delay2.append(0)
            time.sleep(2)
    np.savetxt('delay.txt',delay2,fmt='%3.2f')

def jobcreat(queue,queue2):
    w=0
    job1=[]
    while w<20:
        w+=1
        if queue.qsize()<10:
                batchsize=random.randint(1,2)
                job=[]
                for p in range(0,batchsize):
                    matsize=[2400,2750,2850,2900,2950,3000]
                    dedtim=[20,25,26,28,9,8]
                    mat_size=matsize[random.randint(0,5)]
                    d_tim=dedtim[random.randint(0,5)]
                    job.append(mat_size)
                    job.append(d_tim)
                job.append(time.time())
#                print job
                job1.append(job)
                queue.put(job)
                time.sleep(5)
        else:
            time.sleep(20)

#    np.savetxt('job.txt',job1,delimiter=',')


def vmtimupdation(queue2,queue):
    quesiz=[]
    vmsfree=[]
    No_of_vm=[]
    w=0
    while w<100:
        w+=1
        vms=queue2.get()
        for s in range(0,len(vms)):
            if vms[s]>0:
                vms[s]=vms[s]-1
                if vms[s]<=0:
                    vms[s]=0.0
        queue2.put(vms)
        print vms
        print 'len= ',len(vms)
        print 'Free vms= ', vms.count(0)
        print 'queue size= ',queue.qsize()
        No_of_vm.append(len(vms))    
        vmsfree.append(vms.count(0))
        quesiz.append(queue.qsize())
        time.sleep(1)

    np.savetxt('len.txt',No_of_vm,fmt='%3.0f')
    np.savetxt('vms.txt',vmsfree,fmt='%3.0f')
    np.savetxt('queue.txt',quesiz,fmt='%3.0f')

if __name__ == "__main__":
    queue = Queue()
    queue2 = Queue()
    queue2.put(vms)
    lock=Lock()
    Process(target=jobcreat,args=(queue,queue2)).start()
    Process(target=optialgo,args=(queue,queue2)).start()
    Process(target=vmtimupdation,args=(queue2,queue)).start()
