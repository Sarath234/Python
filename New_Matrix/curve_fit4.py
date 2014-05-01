import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import curve_fit
import math
def func((x,y),k,a,b):
    return k*math.exp(-a*x-b*y)

#data getting and ploting
mat=scipy.io.loadmat('data_detrend.mat')
b=mat['data1']
mat=None
x=b[:,0]
y=b[:,1]
z=b[:,2]
#fig=plt.figure()
#ax=fig.add_subplot(111, projection='3d')
#ax.scatter(x,y,z,c='r',marker='.')
#plt.show()
popt,pcov=curve_fit(func,(x,y),z,p0=(0.1,0.1,0.3))
