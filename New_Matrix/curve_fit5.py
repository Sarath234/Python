import scipy.io
import numpy as np
import matplotlib.pyplot as plt
mat=scipy.io.loadmat('coevsgudness.mat')

b=mat['coevsgudness']
plt.plot(b[:,0],b[:,1])
#plt.
plt.title('Percentage fit vs No of coefficients')
plt.xlabel('No of coefficients')
plt.ylabel('Percentage fit')
plt.grid(True)
plt.show()
