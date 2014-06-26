import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
import matplotlib.pyplot as plt

delay_shared=np.loadtxt('delay_shared.txt')
print 'Shared Algo Total Delay=', sum(delay_shared)
vms_shared=np.loadtxt('vms_shared.txt')
que_shared=np.loadtxt('queue_shared.txt')
lenVM_shared=np.loadtxt('len_shared.txt')
vmsused_shared=lenVM_shared-vms_shared
t1_shared=np.linspace(0,len(vms_shared),num=len(vms_shared))
t2_shared=np.linspace(0,len(delay_shared),num=len(delay_shared))
tq1_shared=np.linspace(0,len(que_shared),num=len(que_shared))

delay=np.loadtxt('delay.txt')
print 'Our Algo Total Delay=', sum(delay)
vms=np.loadtxt('vms.txt')
que=np.loadtxt('queue.txt')
lenVM=np.loadtxt('len.txt')
vmsused=lenVM-vms
t1=np.linspace(0,len(vms),num=len(vms))
t2=np.linspace(0,len(delay),num=len(delay))
t3=np.linspace(0,40,num=40)

fig=plt.figure()
plt.plot(t2_shared,delay_shared,'-*',label="Shared Algorithm")
plt.plot(t2,delay,'-o',label="Proposed Algorithm")
#plt.title('Delay Comparison')
plt.xlabel('Jobs')
plt.ylabel('Delay (in sec)')
plt.grid(True)
plt.legend( loc='best')
#plt.show()

fig=plt.figure()
plt.plot(tq1_shared,que_shared,'-*',label="Shared Algoritham")
plt.plot(t1,que,'-o',label="Proposed Algoritham")
#plt.title('Queue Comparison')
plt.xlabel('Time')
plt.ylabel('Queue Size of Both Algorithms')
plt.grid(True)
plt.legend( loc='best')
#plt.show()

'''fig=plt.figure()
plt.plot(t1_shared,lenVM_shared,'-*',label="Shared Algoritham")
plt.plot(t1,lenVM,'-o',label="Our Algoritham")
plt.title('No of VMs Comparison')
plt.xlabel('Time')
plt.ylabel('No of VMs of Both Algorithms')
plt.grid(True)
plt.legend( loc='upper left')
#plt.show()

fig=plt.figure()
plt.plot(t1_shared,vms_shared,'-*',label="Shared Algoritham")
plt.plot(t1,vms,'-o',label="Our Algoritham")
plt.title('No of Free VMs Comparison')
plt.xlabel('Time')
plt.ylabel('No of Free VMs of Both Algorithms')
plt.grid(True)
plt.legend( loc='upper left')'''

fig=plt.figure()
plt.plot(t1_shared,vmsused_shared,'-*',label="Shared Algorithm")
plt.plot(t1,vmsused,'-o',label="Proposed Algorithm")
#plt.title('Busy VMs Comparison')
plt.xlabel('Time (in sec)')
plt.ylabel('VMs Utilized')
plt.grid(True)
plt.legend( loc='best')
#plt.show()

fig=plt.figure()
plt.plot(t3,tuple(lenVM_shared[0:40]),'-*',label="Shared Algorithm")
plt.plot(t3,tuple(lenVM[0:40]),'-o',label="Proposed Algorithm")
#plt.title('No of VMs Comparison')
plt.xlabel('Time (in sec)')
plt.ylabel('No of VMs')
plt.grid(True)
plt.legend( loc='best')
plt.show()
