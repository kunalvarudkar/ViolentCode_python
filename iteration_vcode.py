# Code for iteration that checks entire ip range for FTP port
#vcode8
#coded by-> payload
import socket
def establish(ip,port):
	try:
		socket.setdefaulttimeout(2)
		s=socket.socket()
		s.connect((ip,port))
		ans=s.recv(1024)
		print ("IP= "+str(ip)+" checking on Port no="+str(port)+" for FTP vulnerability "+str(ans))
	except Exception, e:
		print "For IP="+str(ip)+" having Error:"+str(e)

def main():
	for x in range (1,100):
		ip1="10.10.50."+str(x)
		port=21
		establish(ip1,port)
	
if __name__=='__main__':
	main()
