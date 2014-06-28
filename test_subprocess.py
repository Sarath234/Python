import subprocess,time

import pwd
import grp
import os
uid=pwd.getpwnam('nobody').pw_uid
gid=grp.getgrnam('nogroup').gr_gid

def read_cpu(fil):
    f=open(fil,'r')
    cpu_per=f.read()
    f.close()
    try:
        return float(cpu_per)
    except:
        read_cpu(fil)

def free_vms_update():
    VM_per=[]
    freeVMs=[]
    ips=['192.168.122.245','192.168.122.148','192.168.122.195','192.168.122.65']#,'192.168.122.34','192.168.122.35','192.168.122.128','192.168.122.232','192.168.122.39','192.168.122.191']
    for i in range(4):
        fil=str(i)+'.txt'
        VM_per.append(read_cpu(fil))
    for i in range(len(VM_per)):
        if VM_per[i]<60:
            freeVMs.append(ips[i])
    return freeVMs

freeVMs=free_vms_update()

fil_nam_freeVMs='freeVMs'+str(0)
fw=open(fil_nam_freeVMs,'w')
vm01='192.168.122.142'
fw.write('%s\n' %vm01)
for j in range(0,2):
    print 'freeVMs writing',freeVMs[j]
    fw.write('%s\n' %freeVMs[j])
fw.close()
time.sleep(1)
os.chown(fil_nam_freeVMs,uid,gid)
print 'mpiexec -f '+fil_nam_freeVMs+' -n'+' '+str(2+1)+' python mulpar_new.py 01b1m.txt &'
#per=subprocess.check_output('ssh root@192.168.122.245 nohup mpiexec -f /export/validation_files/'+fil_nam_freeVMs+' -n'+' '+str(2)+' python mulpar_new.py 01b1m.txt &',stderr=subprocess.STDOUT,shell=True)

per=subprocess.check_output('ssh root@192.168.122.245 nohup python /export/validation_files/creatmat.py &',stderr=subprocess.STDOUT,shell=True)
print per

'''s=['01b1m.txt', '01b2m.txt']
argmt=[1, 3]
freeVMs=['192.168.122.245', '192.168.122.148', '192.168.122.195', '192.168.122.65']


def vm1(s,argmt,freeVMs):
    print 's',s
    print 'argmt',argmt
    print 'freeVMs',freeVMs

    for i in range(0,len(s)):
        fil_nam_freeVMs='freeVMs'+str(i)+'.txt'
        fw=open(fil_nam_freeVMs,'w')
        for j in range(0,argmt[i]):
            if i==0:
                print 'freeVMs writing',freeVMs[j]
                fw.write('%s\n' %freeVMs[j])
            else:
                print 'freeVMs writing',freeVMs[j+argmt[i-1]]
                fw.write('%s\n' %freeVMs[j+argmt[i-1]])
        fw.close()
#        for l in range(i,i+argmt[i]-1):
#            del freeVMs[l]

vm1(s,argmt,freeVMs)'''
