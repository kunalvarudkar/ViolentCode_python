import socket
import time
ip='10.10.50.67'
port=21
socket.setdefaulttimeout(2)
s=socket.socket()
s.connect((ip,port))
ans=s.recv(1024)
#print ans
f = open("supportingfile.txt",'r') #open file in read only mode
line=f.readline() #read the file line by line
while line: # till the file has data/lines
        data=line.strip()
	#print data
        if data in ans:
		print "Searching for vulnerable services from File= supportingfile.txt"
		time.sleep(1)
		print "[+]Found Vulnerable service= "+str(ans)+"running on IP address="+str(ip)+" on Port no="+str(port) 	
	line=f.readline() 
f.close() #close the file after use


