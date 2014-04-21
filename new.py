import subprocess
import time
t=time.time()
per=(subprocess.check_output('ssh root@192.168.32.218 nohup python /export/user/psutilexe.py',stdin=None,stderr=subprocess.STDOUT,shell=True)).split(' ')
print 'CPU %=',float(per[0])
print 'MEM %=',float(per[1])
print time.time()-t
