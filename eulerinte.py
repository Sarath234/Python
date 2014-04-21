import numpy as np
import matplotlib.pyplot as plt

t0=0.0
tf=10.0
dt=.1
k=1
b=1
x0=0.5

tvec=np.arange(t0,tf+dt,dt)
xvec=np.zeros(len(tvec))
xvec[0]=x0
for i in range(len(xvec)-1):
    xvec[i+1]=xvec[i]+-k/b*dt*xvec[i]

plt.plot(tvec,xvec,lw=2)
plt.xlabel('time [sec]')
plt.ylabel('x [m]')
plt.show()
plt.close()
plt.clf()
plt.cla()

