import socket
socket.setdefaulttimeout(2)
s=socket.socket() #create INET socket
try:
    s.connect(("192.168.57.128",21))
    #ans=s.recv(1024)

except Exception, e:
    print "[-]Error:"+str(e)

ans=s.recv(1024) #receive 1024 bytes of data
print (ans)

