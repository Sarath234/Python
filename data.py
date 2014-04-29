import sys, math, random, numpy
from numpy import *
import math
import pwd
import grp
import os

def init_board(N):
    X = numpy.array([(round(random.uniform(-10, 10),2), round(random.uniform(-10, 10),2)) for i in range(N)])
    return X

def getRandomCentroids(k):
    c = numpy.array([(random.uniform(-10, 10), random.uniform(-10, 10)) for i in range(k)])
    return c

uid=pwd.getpwnam('nobody').pw_uid
gid=grp.getgrnam('nogroup').gr_gid
B=init_board(int(sys.argv[1]))
print B
savetxt('data.txt',B)
os.chown('data.txt',uid,gid)
centroidlist=getRandomCentroids(int(sys.argv[2]))
print centroidlist
savetxt('centroid.txt',centroidlist)
os.chown('centroid.txt',uid,gid)
