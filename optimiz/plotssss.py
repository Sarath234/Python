import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
import matplotlib.pyplot as plt

delay=np.loadtxt('delay.txt')
vms=np.loadtxt('vms.txt')
que=np.loadtxt('queue.txt')
lenVM=np.loadtxt('len.txt')
t1=np.linspace(0,100,num=100)
t2=np.linspace(0,100,num=20)
fig=plt.figure()
plt.plot(t1,que, label="Queue")
plt.grid(True)
fig=plt.figure()
plt.plot(t1,vms, label="VMs")
plt.grid(True)
fig=plt.figure()
plt.plot(t2,delay, label="Delay")
plt.grid(True)
fig=plt.figure()
plt.plot(t1,lenVM, label="lenVM")
plt.grid(True)
plt.show()
