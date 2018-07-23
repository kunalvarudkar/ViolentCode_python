import socket
socket.setdefaulttimeout(2)
s=socket.socket()
s.connect(("10.10.50.67",21))
ans = s.recv(1024)
print ans
if("vsFTPd 3.0.3" in ans ):
    print "[+]vsFTPD 3.0.3 FTP version is vulnerable."
elif("3Com FTP Server version 2.0" in ans):
    print "[+]3com FTP server 3.0.3 vulnerable."
else:
    print "[-]FTP server not vulnerable"
