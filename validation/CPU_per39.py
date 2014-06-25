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
    fw=open('8.txt','w')
    fw.write('%s\n' %P)
    fw.close()
    try:
        os.chown('8.txt',uid,gid)
    except:
        pass
#    print time.time()-t
    time.sleep(1)
