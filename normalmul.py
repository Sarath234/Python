from numpy import *
import math
import pickle
import time
t=time.time()
#A=pickle.load(open('mat','rb'))
A=loadtxt('mat.txt',delimiter=',')
print dot(A,A)
print time.time()-t
