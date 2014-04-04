#!/usr/bin/env python
from numpy import *
import math
import pickle
import time
from mpi4py import MPI
comm=MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
name = MPI.Get_processor_name()
def part1(w,x,y,z):
    b1=dot(x,y)
    c1=dot(z,b1)
    d1=w-c1
    return linalg.inv(d1)

def part2(a,b,c):
    e1=dot(b,c)
    return -dot(a,e1)

def inve(D):
    l=math.sqrt(D.size)
    D11=matrix(D[:l/2,:l/2])
    D12=matrix(D[:l/2,l/2:l])
    D21=matrix(D[l/2:l,:l/2])
    D22=matrix(D[l/2:l,l/2:l])
    E=zeros_like(D)
    if l/2>=2:
        D11i=inve(D11)
        D22i=inve(D22)
        E11=part1(D11,D22i,D21,D12)
        E22=part1(D22,D11i,D12,D21)
        E12=part2(E11,D12,D22i)
        E21=part2(E22,D21,D11i)
        E[l/2:l,:l/2]=E11
        E[l/2:l,l/2:l]=E12
        E[:l/2,:l/2]=E21
        E[:l/2,l/2:l]=E22
        return E
    else:
        E=linalg.inv(D)
        return E
if rank==0:
    A=pickle.load(open('mat','rb'))
    print A
    C=linalg.inv(A)
    print C
else:
    A = None
A = comm.bcast(A, root=0)
'''if rank==0:
    l=math.sqrt(A.size)
    B=zeros_like(A)
    A11=matrix(A[:l/2,:l/2])
    A12=matrix(A[:l/2,l/2:l])
    A21=matrix(A[l/2:l,:l/2])
    A22=matrix(A[l/2:l,l/2:l])
    A11i=comm.recv(source=1,tag=2)
    A22i=comm.recv(source=1,tag=2)
    B11=part1(A11,A22i,A21,A12)
    B22=part1(A22,A11i,A12,A21)
    B12=part2(B11,A12,A22i)
    B21=part2(B22,A21,A11i)
    B[l/2:l,:l/2]=B11#comm.recv(source=1,tag=1)
    B[l/2:l,l/2:l]=B12#comm.recv(source=1,tag=2)
    B[:l/2,:l/2]=B21#comm.recv(source=1,tag=3)
    B[:l/2,l/2:l]=B22#comm.recv(source=1,tag=4)
    print B'''
if rank==1:
#    print A
#    l=math.sqrt(A.size)
#    B=zeros_like(A)
#    A11=matrix(A[:l/2,:l/2])
#    A12=matrix(A[:l/2,l/2:l])
#    A21=matrix(A[l/2:l,:l/2])
#    A22=matrix(A[l/2:l,l/2:l])
#    A11=comm.recv(source=0,tag=1)
#    A11i=inve(A11)
#    comm.send(A11i,dest=0,tag=2)
#    A22=comm.recv(source=0,tag=1)
#    A22i=inve(A22)
#    print A22i,A11i
#    B11=part1(A11,A22i,A21,A12)
#    B22=part1(A22,A11i,A12,A21)
#    B12=part2(B11,A12,A22i)
#    B21=part2(B22,A21,A11i)
#    B[l/2:l,:l/2]=B11#comm.recv(source=1,tag=1)
#    B[l/2:l,l/2:l]=B12#comm.recv(source=1,tag=2)
#    B[:l/2,:l/2]=B21#comm.recv(source=1,tag=3)
#    B[:l/2,l/2:l]=B22#comm.recv(source=1,tag=4)
    print A
    B=inve(A)
    print B

#    comm.send(A22i,dest=0,tag=2)
