def worker(input_q):
    while True:
        input_q.get()
        
        subprocess.call('mpiexec -n 1 python mulpar1.py &',shell=True)
        print 'I am Worker'
        input_q.task_done()

def master(sequence,output_q):
    for item in sequence:
        subprocess.call('python creatmat.py',shell=True)
        output_q.put(1)
    time.sleep(1)
if __name__== "__main__":
    from multiprocessing import Process, JoinableQueue
    from numpy import *
    import subprocess
    import math
    import pwd
    import grp
    import os,time
    import numpy as np

    q=JoinableQueue()
    con_p=Process(target=worker,args=(q,))
    con_p.daemon=True
    con_p.start()
    sequence=range(4)
    master(sequence,q)
    q.join()
