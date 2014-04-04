from mpi4py import MPI
import numpy
#import pwd
#import grp
#import os
comm=MPI.Comm.Get_parent()
size=comm.Get_size()
rank=comm.Get_rank()
A=numpy.loadtxt('mat.txt',delimiter=',')
l=len(A)
#l=numpy.array(0,'i')
#comm.Bcast([l,MPI.INT],root=0)
#print l
x=numpy.array(0,'i')
comm.Bcast([x,MPI.INT],root=0)
#print x
#A=numpy.zeros((l,l))
#comm.Bcast([A,MPI.INT],root=0)
C=numpy.zeros((l-x,l))
for j in xrange(0,l-x):
    C[j]=numpy.dot(A[j+x],A)
comm.Send(C)
#uid=pwd.getpwnam('nobody').pw_uid
#gid=grp.getgrnam('nogroup').gr_gid

#numpy.savetxt('out.txt',C,delimiter=',',fmt='%3.3f')
#print "Disconnecting from rank %d \n" %rank
#os.chown('out.txt',uid,gid)
C=None
comm.Disconnect()
