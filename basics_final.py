import socket
import sys
import os
import time

def establish(ip,port,filename):
	try:
		socket.setdefaulttimeout(2)
		s=socket.socket()
		s.connect((ip,port))
		ans=s.recv(1024)
		f=open(filename,'r')
        	line=f.readline() #read the file line by line
        	while line: # till the file has data/lines
                	data=line.strip()#print data
                	if data in ans:
                        	print "[+]Searching for vulnerable services from File="+str(filename)
                        	time.sleep(1)
                        	print "[+]Found Vulnerable service= "+str(ans)+"running on IP address="+str(ip)+" on Port no="+str(port)
                	line=f.readline()
        	f.close() #close the file after use

	except Exception ,e:
		print "[-]IP:"+str(ip)+" is having Error: "+str(e)+" at Port no:"+str(port)

def checkfile(filename):
	if not os.path.isfile(filename):
		print "[-]File does not exist[-]"
		exit(0)
	if not os.access(filename,os.R_OK):
		print "[-]File:"+str(filename)+" dont have read access"
		exit(0)


def main():
	port=21
	if len(sys.argv)==2:
		filename=sys.argv[1]
		checkfile(filename)
	for i in range(1,255):
		ip="192.168.50."+str(i)
		establish(ip,port,filename)

if __name__=='__main__':
	main()
