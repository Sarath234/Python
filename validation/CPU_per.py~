import psutil
import pwd
import grp
import os,time
import numpy as np
uid=pwd.getpwnam('nobody').pw_uid
gid=grp.getgrnam('nogroup').gr_gid
while True:
    t=time.time()
    P=psutil.cpu_percent()
    if P>50:
        fw=open('0.txt','w')
        fw.write('%s\n' %P)
        fw.close()
        os.chown('0.txt',uid,gid)
#    print time.time()-t
    time.sleep(1)
