import subprocess
per=subprocess.check_output('ssh root@192.168.32.218 nohup python /export/user/psutilexe.py',stdin=None,stderr=subprocess.STDOUT,shell=True)
print 'CPU %=',per
