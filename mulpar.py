from numpy import *
import math
from mpi4py import MPI
import time
import subprocess,sys
t=time.time() #to get computation time

comm=MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
A=loadtxt(sys.argv[1],delimiter=',') # A Matrix 
#print A
l=len(A) #No of Rows
n=len(A)/size #No of rows for Each processor
rem=len(A)%size #Remaining rows

if rem==0:
    a=rank*n
    b=a+n
    C=dot(A[a:b,:],A)

else:
    if rank!=size-1:
        a=rank*n
        b=a+n
        C=dot(A[a:b,:],A)
    else:
        a=rank*n
        D=dot(A[a:len(A),:],A)

if rank==0:
    subprocess.call('rm '+sys.argv[1],shell=True)
    E=zeros_like(A)
    E[a:b,:]=C
    if rem==0:
        for i in range(1,size):
            E[i*n:(i*n)+n,:]=comm.recv(source=i)
    else:
        for i in range(1,size):
            if i!=size-1:
                E[i*n:(i*n)+n,:]=comm.recv(source=i)
            else:
                E[i*n:len(A),:]=comm.recv(source=size-1)
else:
    if rem==0:    
        comm.send(C)
    else:
        if rank!=size-1:
            comm.send(C)
        else:
            comm.send(D)
if rank==0:
    print E
    print time.time()-t
