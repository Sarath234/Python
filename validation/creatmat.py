from numpy import *
import cPickle as pickle
import math
import pwd
import grp
import os
import numpy as np
uid=pwd.getpwnam('nobody').pw_uid
gid=grp.getgrnam('nogroup').gr_gid
A=np.random.uniform(size=(2400,2400)).astype('d')
print A
print np.dot(A,A)
savetxt('mat.txt',A,delimiter=',',fmt='%3.3f')
os.chown('mat.txt',uid,gid)
