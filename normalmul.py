from numpy import *
import math
import pickle
import time
t=time.time()
A=pickle.load(open('mat','rb'))
print dot(A,A)
print time.time()-t
