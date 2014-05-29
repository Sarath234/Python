#!/usr/bin/python
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('localhost',8081))
s.send('Hi...!')
data=s.recv(1024)
s.close()
print 'Recieved: '
print data
