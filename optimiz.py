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

vms=[0.0]*10

def vm1(vms,argmt,minv):
    vm=[]
    vms=sorted(vms)
    for i in range(0,len(argmt)):
        for j in range(0,argmt[i]):
            vm.append(minv[i])
#    print vm
#    print vms
    for i in range(0,len(vm)):
        vms[i]=vm[i]
    return vms

def find_time(a,b):
    for i in range(0,len(x[:,0])):
        if a==x[i,0]:
            if b==y[i,0]:
#                print z[i,0]
                return z[i,0]

def creatmat(queue,queue2):
    delay2=[]
    x=0
    while x<20:
        x+=1
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
#	    print s,'\n',dt,'\n',tim
        
            A=np.zeros(shape=(len(s),10))
            for j in range(1,11):
	        for k in range(0,len(s)):
                    ab=find_time(s[k],j)-dt[k]
		    if(ab>0):
                        A[k,j-1]=ab
                    else:
                        A[k,j-1]=0
#            print A
            N=vms.count(0)
#            print N
#            N=10
            y=0
            delay=0
            argmt=[]
            minv=[]
            for l in range(0,A.shape[0]):
                argmt.append(np.argmin(A[l,:]))
                minv.append(np.min(A[l,:]))
                y=y+(np.argmin(A[l,:])+1)
                delay=delay+np.min(A[l,:])
#            print argmt
#            print minv
            if y<=N:
                if vms.count(0.0)==0:
                    time.sleep(np.min(vms))
                    vms=vm1(vms,argmt,minv)
                else:
                    vms=vm1(vms,argmt,minv)
                for i in range(0,len(argmt)):
                    for j in range(0,argmt[i]):
                        vms[i]=minv[i]
                print "No Dealy"
#                print vms
                delay2.append(time.time()-tim)
                queue2.put(vms)

            else:
                extradelay=[]
                J_lis=[]
                minv=[]
                N=vms.count(0)
#                print "VMs are free= ", N
                excess=y-N
#                print excess
                for m in range(0,A.shape[0]):
                    J=np.argmin(A[m,:])
                    extradelay.append(A[m,J-1]-A[m,J])
                    J_lis.append(J)
#                print J_lis,'\n',extradelay
                while excess>0:
                    I=np.argmin(extradelay)
                    J=J_lis[I]
                    extradelay[I]=A[I,J-1]-A[I,J]
                    excess=excess-1
        	    J_lis[I] = J-1
#                print J_lis,'\n',extradelay
                delay=0
                for p in range(0,A.shape[0]):
#                    print A[p,J_lis[p]-1]
                    delay=delay+A[p,J_lis[p]-1]
                    minv.append(A[p,J_lis[p]-1])
                delay2.append(time.time()-tim+delay)
#                np.savetxt('delay.txt',delay2,fmt='%3.2f')
                print 'Total Delay= ', time.time()-tim+delay,'Delay Test= ',delay
                for q in range(0,len(J_lis)):
                    J_lis[q]=J_lis[q]+1
                if vms.count(0.0)==0:
#                    print np.min(vms)
                    time.sleep(np.min(vms))
                    vms=vm1(vms,J_lis,minv)
                else:
                    vms=vm1(vms,J_lis,minv)
#                print vms
                queue2.put(vms)
            time.sleep(5)
        else:
            print 'Queue is Empty'
            time.sleep(2)
    np.savetxt('delay.txt',delay2,fmt='%3.2f')

def jobcreat(queue):
    x=0
    while x<20:
        x+=1
        if queue.qsize()<10:
            batchsize=random.randint(1,5)
            job=[]
            for p in range(0,batchsize):
                matsize=[2400,2750,2850,2900,2950,3000]
                dedtim=[9,10,8,7,5,4,6]
                mat_size=matsize[random.randint(0,5)]
                d_tim=dedtim[random.randint(0,5)]
                job.append(mat_size)
                job.append(d_tim)
            job.append(time.time())
#            print job
            queue.put(job)
            time.sleep(5)
        else:
            time.sleep(200)

def vmtimupdation(queue2,queue):
    quesiz=[]
    vmsfree=[]
    x=0
    while x<100:
        vms=queue2.get()
        for s in range(0,len(vms)):
            if vms[s]>0:
                vms[s]=vms[s]-1
                if vms[s]<0:
                    vms[s]=0.0
#        print vms
#        print 'Free vms= ', vms.count(0)
#        print 'queue size= ',queue.qsize()
        vmsfree.append(vms.count(0))
        quesiz.append(queue.qsize())
        queue2.put(vms)
        x+=1
        time.sleep(1)

    np.savetxt('vms.txt',vmsfree,fmt='%3.0f')
    np.savetxt('queue.txt',quesiz,fmt='%3.0f')

if __name__ == "__main__": 
    queue = Queue()
    queue2 = Queue()
    queue2.put(vms)
    lock=Lock()
    Process(target=jobcreat,args=(queue,)).start()
    Process(target=creatmat,args=(queue,queue2)).start()
    Process(target=vmtimupdation,args=(queue2,queue)).start()
