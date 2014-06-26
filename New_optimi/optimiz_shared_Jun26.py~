import numpy as np
import scipy.io
from multiprocessing import Process, Lock, Queue
import random,time,pickle

mat=scipy.io.loadmat('simulation1.mat')
b=mat['simulationdata']
mat=None
x=b[:,0]
y=b[:,1]
z=b[:,2]
x=x.reshape(60,1)
y=y.reshape(60,1)
z=z.reshape(60,1)

vms=[0]*5
#vms[0]=12

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


def find_tim(a,b):
    for i in range(0,len(x[:,0])):
        if a==x[i,0]:
            if b==y[i,0]:
#                print z[i,0]
                return z[i,0]

def sharedalgo(queue,queue2):
    delay2=[]
    while True:
        if queue.qsize()!=0:
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
            vms=queue2.get()
            queue2.put(vms)
            K=vms.count(0.0)
            while vms.count(0)<len(s):
                vms=queue2.get()
                queue2.put(vms)

                freVMs=vms.count(0)
                Ln_vms=len(vms)
                req_vms=len(s)-freVMs
#                print 'free vms ', freVMs
#                print 'lenght of jobs ', len(s)
#                print 'required vms ', req_vms

                if Ln_vms<10:
                    if Ln_vms+req_vms>10:
                        vms=queue2.get()
                        for i in range(0,10-Ln_vms):                        
                            vms.append(0)
                        queue2.put(vms)
                        req_vms=0
                    else:
                        vms=queue2.get()
                        for i in range(0,req_vms):
                            vms.append(0)
                        queue2.put(vms)
                        req_vms=0
                elif Ln_vms==10:
                    while req_vms>0:
#                        print '\n reached exactly 10 vms'
#                        print '\n req vms = ' , req_vms
			vms=queue2.get()
#			print '\n vms = ', vms
			queue2.put(vms)
                        time.sleep(np.min(vms))
                        frvm=vms.count(0)
#			print 'free vms = ', frvm
#                        print 'Im Working'
                        req_vms=req_vms-frvm
#			print '\n vms 1 = ' ,vms

            vms=queue2.get()
            queue2.put(vms)
            N=vms.count(0.0)
            rem=N%len(s)
            D=N/len(s)
#            print 'rem',rem
            NOV=[]
#            print D
            if rem==0:
                for i in range(0,len(s)):
                    NOV.append(D)
            else:
                for j in range(0,rem):
                    NOV.append(D+1)
                for j in range(rem,len(s)):
                    NOV.append(D)
#            print NOV
            delay=0
            time1=[]
            for i in range(0,len(s)):
                time1.append(find_tim(s[i],NOV[i]))
                ab=time1[i]-dt[i]
                if ab>=0:
                    delay=delay+ab
                else:
                    delay=delay
            delay2.append(time.time()-tim+delay)
            print "Delay New= ",time.time()-tim+delay
            vms=queue2.get()
            vms=vm1(vms,NOV,time1)
            queue2.put(vms)
        np.savetxt('delay_shared.txt',delay2,fmt='%3.2f')

def jobcreat(queue,queue2):
    job1=[]
    data=pickle.load(open('job11.txt','rb'))
    for i in data:
#            job.append(i)
#            print i
        i.append(time.time())
#            print i
#        print 'job',i
        queue.put(i)
        time.sleep(5)


'''def jobcreat(queue,queue2):
    w=0
    job1=[]
    job_run=True
    while w<50:
        w+=1
        if queue.qsize()<10:
                batchsize=random.randint(1,2)
                job=[]
                for p in range(0,batchsize):
                    matsize=[2400,2750,2850,2900,2950,3000]
                    dedtim=[20,15,16,25,10,9,8]
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
    job_run=False
#    np.savetxt('job.txt',job1,delimiter=',')'''

def vmtimupdation(queue2,queue):
    quesiz=[]
    vmsfree=[]
    No_of_vm=[]
    while True:
        vms=queue2.get()
        for s in range(0,len(vms)):
            if vms[s]>0:
                vms[s]=vms[s]-1
                if vms[s]<=0:
                    vms[s]=0.0
        queue2.put(vms)
        print sorted(vms)
#        print 'len= ',len(vms)
#        print 'Free vms= ', vms.count(0)
        print 'queue size= ',queue.qsize()
#        print 'w= ',w
        No_of_vm.append(len(vms))    
        vmsfree.append(vms.count(0))
        quesiz.append(queue.qsize())
        time.sleep(1)

        np.savetxt('len_shared.txt',No_of_vm,fmt='%3.0f')
        np.savetxt('vms_shared.txt',vmsfree,fmt='%3.0f')
        np.savetxt('queue_shared.txt',quesiz,fmt='%3.0f')

'''def vmtimupdation(queue2,queue):
    quesiz=[]
    vmsfree=[]
    No_of_vm=[]
    w=0
    while w<180:
        w+=1
        vms=queue2.get()
        for s in range(0,len(vms)):
            if vms[s]>0:
                vms[s]=vms[s]-1
                if vms[s]<=0:
                    vms[s]=0.0
        queue2.put(vms)
        print vms
        print 'w=',w
        print 'len= ',len(vms)
        print 'Free vms= ', vms.count(0)
        print 'queue size= ',queue.qsize()
        No_of_vm.append(len(vms))    
        vmsfree.append(vms.count(0))
        quesiz.append(queue.qsize())
        time.sleep(1)
        np.savetxt('len_shared.txt',No_of_vm,fmt='%3.0f')
        np.savetxt('vms_shared.txt',vmsfree,fmt='%3.0f')
        np.savetxt('queue_shared.txt',quesiz,fmt='%3.0f')'''

if __name__ == "__main__": 
    queue = Queue()
    queue2 = Queue()
    queue2.put(vms)
    lock=Lock()
    Process(target=jobcreat,args=(queue,queue2)).start()
    Process(target=sharedalgo,args=(queue,queue2)).start()
    Process(target=vmtimupdation,args=(queue2,queue)).start()
