import scipy.io
import numpy as np
mat=scipy.io.loadmat('data_detrend.mat')
b=mat['data1']
#mat=None
#b=np.loadtxt('data_est.txt',delimiter=',')
#print b[:,2]
x=b[:,0]
y=b[:,1]
#z=b[:,2]
z=2.30304810587*np.exp(-(-0.00114024112986*x+ 0.841791952745*y-0.173758152165*y**2+0.0165197711845*y**3-0.000593948124453*y**4))
print z
