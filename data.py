import sys, math, random, numpy
from numpy import *
import math
import pwd
import grp
import os
import numpy as np
import matplotlib

def init_board(N):
    X = numpy.array([(round(random.uniform(-10, 10),2), round(random.uniform(-10, 10),2)) for i in range(N)])
    return X

uid=pwd.getpwnam('nobody').pw_uid
gid=grp.getgrnam('nogroup').gr_gid
B=init_board(1000)
print B
savetxt('data.txt',B)
os.chown('data.txt',uid,gid)

