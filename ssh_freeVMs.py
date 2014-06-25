import subprocess
import numpy as np
f=open('hosts','r')
data=f.read()
f.close()
data=data.split('\n')
#print len(data)
#print data
freeVMs=[]
for i in range(len(data)-1):
    per=(subprocess.check_output('ssh root@'+data[i]+' '+'nohup python /export/user/psutilexe.py',stdin=None,stderr=subprocess.STDOUT,shell=True)).split(' ')
#    print 'CPU %=',float(per[0])
#    print 'MEM %=',float(per[1])
    if float(per[0])<90:
        freeVMs.append(data[i])
print freeVMs
fw=open('freeVMs','w')
for i in freeVMs:
    fw.write('%s\n' %i)
fw.close()
