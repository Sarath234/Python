from numpy import *
import math
from mpi4py import MPI
import time
import subprocess,sys
t=time.time() #to get computation time

comm=MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

#Broadcasting A

if rank==0:
    A=loadtxt(sys.argv[1],delimiter=',') # A Matrix
else:
    A=None
A=comm.bcast(A,root=0)
rem=len(A)%(size-1)

if rank==0:
    l=len(A) #No of Rows
    n=len(A)/(size-1) #No of rows for Each processor
    for j in range(1,size):
        if rem==0:
            a=(j-1)*n
            b=a+n
            comm.send(A[a:b,:],dest=j)
        else:
            if j!=size-1:
                a=(j-1)*n
                b=a+n
                comm.send(A[a:b,:],dest=j)
            else:
                a=(j-1)*n
                comm.send(A[a:len(A),:],dest=size-1)
else:
    C=dot(comm.recv(source=0),A)

if rank==0:
    #subprocess.call('rm '+sys.argv[1],shell=True)
    E=zeros_like(A)
    if rem==0:
        for i in range(1,size):
             E[(i-1)*n:((i-1)*n)+n,:]=comm.recv(source=i)
    else:
        for i in range(1,size):
            if i!=size-1:
                E[(i-1)*n:((i-1)*n)+n,:]=comm.recv(source=i)
            else:
                E[(i-1)*n:len(A),:]=comm.recv(source=size-1)
else:
    comm.send(C)
if rank==0:
    print E
    print time.time()-t
