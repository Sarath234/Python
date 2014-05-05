import numpy as np
import scipy.io
from multiprocessing import Process, Lock, Queue
import random,time

mat=scipy.io.loadmat('data_detrend.mat')
b=mat['data1']
mat=None
x=b[:,0]
y=b[:,1]
z=b[:,2]
x=x.reshape(348,1)
y=y.reshape(348,1)
z=z.reshape(348,1)

def find_time(a,b):
    for i in range(0,len(x[:,0])):
        if a==x[i,0]:
            if b==y[i,0]:
                return z[i,0] #.astype(int)

def delaymin(A,N):
    y=0
    delay=0
    for l in range(0,A.shape[0]):
        np.argmin(A[l,:])
        y=y+np.argmin(A[l,:])+1
        delay=delay+np.min(A[l,:])
    if y<=N:
        print "No Dealy", 
    else:
        extradelay=[]
        J_lis=[]
        for m in range(0,A.shape[0]):
            J=np.argmin(A[m,:])+1
            extradelay.append(A[m,J]-A[m,J-1])
            J_lis.append(J)
        excess=y-N
        while excess>0:
            I=np.argmin(extradelay)
            J=J_lis[I]-1
            extradelay[I]=A[I,J]-A[I,J-1]
            excess=excess-1
	    J_lis[I] = J
        delay=0
        for i in range(0,A.shape[0]):
            delay=delay+A[i,J_lis[i]]
        print 'Total Delay= ',delay
def creatmat(queue):
    x=0
    while x<20:
        if queue.qsize()!=0:
            quejob=queue.get()
            i = len(quejob)/2
	    s = []
  	    dt = []
	    while (i>0):
                s.append(quejob[2*i-2])
                dt.append(quejob[2*i-1])
		i = i - 1
            A=np.zeros(shape=(len(s),10))
            for j in range(1,11):
	        for k in range(0,len(s)):
		    ab =find_time(s[k],j)-dt[k]
		    if(ab>0):
                        A[k,j-1]=ab
                    else:
                        A[k,j-1]=0
            print A
            N=20
            delaymin(A,N)
        else:
            print 'Queue is Empty'
        time.sleep(5)

def jobcreat(queue):
    x=0
    while x<5:
        batchsize=random.randint(1,5)
        job=[]
        for p in range(0,batchsize):
            matsize=[3000,2850,2750,2650,2550,2400,2350]
            dedtim=[9,10,8,7,5,4,6]
            x=x+1
            mat_size=matsize[random.randint(0,6)]
            d_tim=dedtim[random.randint(0,6)]
            job.append(mat_size)
            job.append(d_tim)
        print job
        queue.put(job)

if __name__ == "__main__": 
    queue = Queue()
    Process(target=jobcreat,args=(queue,)).start()
    Process(target=creatmat,args=(queue,)).start()
#    B=np.random.uniform(size=(10,3)).astype('d')
#    print B
#    delaymin(B)
