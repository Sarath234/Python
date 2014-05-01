import scipy.io
import numpy as np
import matplotlib.pyplot as plt

def my_range(start,end,step):
    while start<=end:
        yield start
        start+=step

mat=scipy.io.loadmat('rawdata.mat')
b=mat['b']
mat=None
x=b[:,0]
y=b[:,1]
z=b[:,2]
b=None
temp1=[]
temp2=[]
temp3=[]
for i in my_range(0,410,10):
    temp1.append(y[i:i+10])
    temp2.append(z[i:i+10])
    temp3.append(x[i:i+10])
c = {40,37,28,22,11}
p=['--','--o','--*','->','-^']
for i, l in enumerate(c):
        print temp1[l],temp2[l],temp3[l]
	plt.plot(temp1[l],temp2[l],p[i],label=str(temp3[l][1]))
plt.legend( loc='upper right', numpoints = 1 )
plt.title('Response Time vs No of VMs')
plt.xlabel('No of VMs')
plt.ylabel('Response Time for Different Matrix Sizes')
plt.grid(True)
plt.show()
