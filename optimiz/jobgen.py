import numpy as np
import random,time
import pickle
import os

def jobcreat():
    w=0
    job1=[]
    while w<20:
        w+=1
        batchsize=random.randint(1,3)
        job=[]
        for p in range(0,batchsize):
            matsize=[2400,2750,2850,2900,2950,3000]
            dedtim=[20,10,15,5,15,8]
            mat_size=matsize[random.randint(0,5)]
            d_tim=dedtim[random.randint(0,5)]
            job.append(mat_size)
            job.append(d_tim)
#        job.append(time.time())
        print job
        job1.append(job)
    pickle.dump(job1,open('job11.txt','wb'))

def main():
    jobcreat()
    data=pickle.load(open('job11.txt','rb'))
    print data, '\n\n\n\n'
    for i in data:
	print i

main()
