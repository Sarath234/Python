import scipy.io
import numpy as np
import matplotlib.pyplot as plt

def my_range(start,end,step):
    while start<=end:
        yield start
        start+=step

mat=scipy.io.loadmat('c.mat')
b=mat['c']
mat=None
x=b[:,0]
y=b[:,1]
z=b[:,2]
b=None
temp1=[]
temp2=[]
temp3=[]
for i in my_range(0,225,25):
    temp1.append(y[i:i+25])
    temp2.append(z[i:i+25])
    temp3.append(x[i:i+25])

c = {1,2,3,4}
p=['--o','->','--*','-^']
for i, l in enumerate(c):
    plt.plot(temp3[l],temp2[l],p[i],label=str(temp1[l][1]))
plt.legend( loc='upper left')
plt.title('Response Time vs Size of Data')
plt.xlabel('Size of Data')
plt.ylabel('Response Time for Different no of VMs')
plt.grid(True)
plt.show()
