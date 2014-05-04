import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import matplotlib
#data getting and ploting
mat=scipy.io.loadmat('data_detrend.mat')
b=mat['data1']
mat=None
x=b[:,0]
y=b[:,1]
z=b[:,2]
b=None
fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')
scatter1=ax.scatter(x,y,z,c='r',marker='+')
scatter1_proxy=matplotlib.lines.Line2D([0],[0],linestyle='none',c='r',marker='+')
x_m=x.reshape(348,1)
y_m=y.reshape(348,1)
z_m=z.reshape(348,1)
x=None
y=None
z=None

#curve fitting
sol=[]
A=np.random.uniform(size=(348,5))
lnz=np.transpose(np.matrix(np.log(z_m[:,0])))
p=np.ones_like(x_m)

#A Matrix
y_m2=y_m**2
y_m3=y_m**3
y_m2=y_m2.reshape(348,1)
y_m3=y_m3.reshape(348,1)
A[:,0]=p[:,0]
A[:,1]=-x_m[:,0]
A[:,2]=-y_m[:,0]
A[:,3]=-y_m2[:,0]
A[:,4]=-y_m3[:,0]
#Lst_square fit
AT=np.transpose(A)
prod=np.dot(AT,A)
inv1=np.linalg.inv(prod)
prod1=np.dot(inv1,AT)
sol=np.dot(prod1,lnz)
#print sol
k=math.exp(sol[0])
a=sol[1]
b=sol[2]
c=sol[3]
d=sol[4]
z_est=k*(np.exp(-a*x_m[:,0]-b*y_m[:,0]-c*y_m2[:,0]-d*y_m3[:,0]))
z_est=np.transpose(z_est)
#goodness of fit
scipy.io.savemat('data_est.mat',{'x':x_m,'y':y_m,'z':z_est})
mat=scipy.io.loadmat('data_est.mat')
x_m=mat['x']
y_m=mat['y']
z_est=mat['z']
mat=None
error=z_est-z_m
SSE=sum(error*error)
RMSE=math.sqrt(np.mean(error*error))
print 'RootMeanSquareError= ',RMSE
print 'SSE= ',SSE[0]
z_av=np.mean(z_m)
error2=z_est-z_av
SST=sum(error2*error2)
RSquare=1-(SSE/SST)
print 'RSquare= ',RSquare[0]
print 'z=',k,'*exp(-(',a[0,0],'x+',b[0,0],'y',c[0,0],'y^2+',d[0,0],'y^3))'#,e[0,0],'y^4))'
#ploting estimated
scatter2=ax.scatter(x_m,y_m,z_est,c='g',marker='o')
scatter2_proxy=matplotlib.lines.Line2D([0],[0],linestyle='none',c='g',marker='o')
ax.legend([scatter1_proxy,scatter2_proxy],['Real','Estimated'])
ax.set_xlabel('Matrix Size')
ax.set_ylabel('No of VMs')
ax.set_zlabel('Response Time')
plt.show()
