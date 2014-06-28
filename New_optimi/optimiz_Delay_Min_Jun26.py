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
    delay2=[]
    while True:
        if queue.qsize()!=0:
#            vms=queue2.get()
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

#	    print '\n vms 2 = ' ,vms
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
#            print 'minv= ',minv
            if y<=N:
#                print argmt
#                print minv
                minvv=[]
                for i in range(0,len(s)):
                    minvv.append(find_tim(s[i],argmt[i]))
                vms=queue2.get()
                vms=vm1(vms,argmt,minvv)
#                print 'if',vms
                queue2.put(vms)
                delay_if=0
                for i in range(0,len(s)):
                    xyz=minvv[i]-dt[i]
                    if xyz>=0:
                        delay_if=delay_if+minvv[i]-dt[i]
                    else:
                        delay_if=delay_if
                delay2.append(time.time()-tim+delay_if)
                print "Delay New in if= ",time.time()-tim+delay_if
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
#		print 'Algo Begin \n\n'                
		while excess>0 and truth_value==True:
#                    print 'excess \n', excess    
#                    print '\n A \n \n', A
		    I=np.argmin(extradelay)
#		    print '\n I ', I 
#		    print '\n argmt ', argmt
                    if argmt[I] != 1:
			argmt[I]=argmt[I]-1
#		        print '\n val ', A[I,argmt[I]-2] 
                        extradelay[I]=A[I,argmt[I]-2]-A[I,argmt[I]-1]
                        excess=excess-1
		    else:
 		        max2 = np.max(extradelay)+1
			extradelay[I] = max2
                    truth=0
                    for m in range(0,len(argmt)):
                        truth=truth+argmt[m]
                    if truth==len(argmt):
                        truth_value=False 
#                print 'extradelay list', extradelay

                minvv=[]
#                print 'argmt ',argmt
#                print 'minv ',minv
#                print s
                for i in range(0,len(argmt)):
#                    print argmt[i]
#                    print s[i]
                    minvv.append(find_tim(s[i],argmt[i]+1))
                vms=queue2.get()
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
                delay2.append(time.time()-tim+delay)
                print 'delay New= ',delay+time.time()-tim
        np.savetxt('delay.txt',delay2,fmt='%3.2f')

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
