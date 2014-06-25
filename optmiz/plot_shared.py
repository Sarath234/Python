import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
import matplotlib.pyplot as plt

delay=np.loadtxt('delay_shared.txt')
vms=np.loadtxt('vms_shared.txt')
que=np.loadtxt('queue_shared.txt')
lenVM=np.loadtxt('len_shared.txt')
vmsused=lenVM-vms
t1=np.linspace(0,180,num=180)
t2=np.linspace(0,21,num=21)

fig=plt.figure()
plt.plot(t1,que, label="Queue")
plt.title('Queue Size vs Time')
plt.xlabel('Time')
plt.ylabel('Queue Size')
plt.grid(True)

fig=plt.figure()
plt.plot(t1,vms, label="VMs")
plt.title('Free VMs vs Time')
plt.xlabel('Time')
plt.ylabel('No of Free VMs')
plt.grid(True)

fig=plt.figure()
plt.plot(t2,delay, label="Delay")
plt.title('Delay vs Time')
plt.xlabel('Time')
plt.ylabel('Delay')
plt.grid(True)

fig=plt.figure()
plt.plot(t1,lenVM, label="lenVM")
plt.title('Total No of VMs vs Time')
plt.xlabel('Time')
plt.ylabel('Total No of VMs')
plt.grid(True)

fig=plt.figure()
plt.plot(t1,vmsused, label="lenVM")
plt.title('Engaged VMs vs Time')
plt.xlabel('Time')
plt.ylabel('No of Engaged VMs')
plt.grid(True)
plt.show()
