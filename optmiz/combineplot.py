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
t1_shared=np.linspace(0,180,num=180)
t2_shared=np.linspace(0,21,num=21)

delay=np.loadtxt('delay.txt')
print 'Our Algo Total Delay=', sum(delay)
vms=np.loadtxt('vms.txt')
que=np.loadtxt('queue.txt')
lenVM=np.loadtxt('len.txt')
vmsused=lenVM-vms
t1=np.linspace(0,180,num=150)
t2=np.linspace(0,21,num=21)

fig=plt.figure()
plt.plot(t2_shared,delay_shared,'-*',label="Shared Algoritham")
plt.plot(t2,delay,'-o',label="Our Algoritham")
plt.title('Delay Comparison')
plt.xlabel('Time')
plt.ylabel('Delay of Both Algorithms')
plt.grid(True)
plt.legend( loc='upper left')
#plt.show()

fig=plt.figure()
plt.plot(t1_shared,que_shared,'-*',label="Shared Algoritham")
plt.plot(t1,que,'-o',label="Our Algoritham")
plt.title('Queue Comparison')
plt.xlabel('Time')
plt.ylabel('Queue Size of Both Algorithms')
plt.grid(True)
plt.legend( loc='upper left')
#plt.show()

fig=plt.figure()
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
plt.legend( loc='upper left')

fig=plt.figure()
plt.plot(t1_shared,vmsused_shared,'-*',label="Shared Algoritham")
plt.plot(t1,vmsused,'-o',label="Our Algoritham")
plt.title('Busy VMs Comparison')
plt.xlabel('Time')
plt.ylabel('No of Busy VMs of Both Algorithms')
plt.grid(True)
plt.legend( loc='upper left')
plt.show()
