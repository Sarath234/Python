import scipy.io
import numpy as np
import matplotlib.pyplot as plt

def my_range(start,end,step):
    while start<=end:
        yield start
        start+=step

mat=scipy.io.loadmat('kmeans.mat')
b=mat['b']
mat=None
x=b[:,0]
y=b[:,1]
z=b[:,2]
b=None
temp1=[]
temp2=[]
temp3=[]
for i in my_range(0,225,9):
    temp1.append(y[i:i+9])
    temp2.append(z[i:i+9])
    temp3.append(x[i:i+9])
c = {23,19,14,11,5}
p=['->','-^','--*','--o','--']
for i, l in enumerate(c):
	plt.plot(temp1[l],temp2[l],p[i],label=str(temp3[l][1]))
plt.legend( loc='upper right', numpoints = 1 )
plt.title('Response Time vs No of VMs')
plt.xlabel('No of VMs')
plt.ylabel('Response Time for Different Data Sizes')
plt.grid(True)
plt.show()
