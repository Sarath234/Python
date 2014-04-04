from mpi4py import MPI
import numpy
import sys

A=numpy.loadtxt('mat.txt',delimiter=',')
result=numpy.zeros_like(A)
l=len(A)
x=0
for i in range(len(A)):
    if x<2:
        result[i]=numpy.dot(A[i],A)
        x+=1
    else:
        break
print numpy.dot(A,A)
A=None
comm=MPI.COMM_SELF.Spawn(sys.executable,args=['worker.py','hosts'],maxprocs=1)
#l=numpy.array(len(A),'i')
#comm.Bcast([l,MPI.INT],root=MPI.ROOT)
x=numpy.array(x,'i')
comm.Bcast([x,MPI.INT],root=MPI.ROOT)
#comm.Bcast([A,MPI.INT],root=MPI.ROOT)
C=numpy.zeros((l-x,l))
comm.Recv(C)
#print numpy.loadtxt('out.txt',delimiter=',')
#print C
for j in range(x,l):
    result[j]=C[j-x]
print result
result=None
C=None
comm.Disconnect()
