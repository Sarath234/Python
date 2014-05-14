import numpy as np
from mpi4py import MPI
import math
import sys

comm=MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

def my_range(start,end,step):
    while start<=end:
        yield start
        start+=step

def split_data2(data, pivots):
    assert type(data) is list, "Data is not a list"
    index = 0;
    i = 0;
    breakpoint = []
    while((index<len(data))and(i<len(pivots))):
        if (pivots[i]>=data[index]):
            index+=1
        else:
            breakpoint.append(index)
            i+=1
    ind_start = 0

    x = []
    for i in range(0,len(breakpoint)):
        ind_end = breakpoint[i]
        x.append(data[ind_start:ind_end])          
        ind_start = breakpoint[i]
    x.append(data[ind_start:len(data)])
    return x

if rank==0:
    data=np.random.randint(10000,size=21474836)
    print 'Data= ',data
    len_data=len(data)
    p=size-1
    n=float(len(data))/(p)
    n=math.ceil(n)
    for i in range(1,size):
        a=(i-1)*n
        b=a+n
        comm.send(data[a:b],dest=i,tag=0)
        comm.send(len_data,dest=i,tag=1)
    samples=[]
    for i in range(1,size):
        samples=samples+comm.recv(source=i)
    samples= sorted(samples)
    #print 'samples= ',samples
    send_pivts=[]
    p_2=math.floor(p/2.0)
    for j in my_range(p+p_2-1,(p-1)*p+p_2,p):
        #print j
        send_pivts.append(samples[int(j)])
    #print send_pivts
    for i in range(1,size):
        comm.send(send_pivts,dest=i)
    sorted_list=[]
    for i in range(1,size):
        sorted_list=sorted_list+comm.recv(source=i,tag=5)
    print 'sorted_list=',sorted_list
    
else:
    data_recv=comm.recv(source=0,tag=0)
    n=comm.recv(source=0,tag=1)    
    #print 'data_recv= ',data_recv
    #print len_data
    data_sort=sorted(data_recv)
    #print 'data_sort=',data_sort
    send_samples=[]
    p=size-1
    for i in my_range(0,(p-1)*(n/p**2),n/p**2):
        send_samples.append(data_sort[i])
    #print "send_sample=",send_samples
    comm.send(send_samples,dest=0)
    pivts=comm.recv(source=0)
#    print 'pivts= ',pivts
    x= split_data2(data_sort,pivts)
#    print 'x=',x
    temp=[]
    for i in range(0,len(x)):
        if (i+1)!=rank:
            comm.send(x[i],dest=i+1)
        else:
            temp=temp+x[i]
    for i in range(0,size-1):
        if (i+1)!=rank:
            temp=temp+comm.recv(source=i+1)
        else:
            pass
    temp=sorted(temp)
#    print 'temp=',temp,'rank=',rank
    comm.send(temp,dest=0,tag=5)
