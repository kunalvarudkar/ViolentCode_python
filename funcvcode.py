import socket
def establish(ip,port):
	try:
		socket.setdefaulttimeout(2)
		s=socket.socket()
		s.connect((ip,port))
		ans=s.recv(1024)
		print "IP="+str(ip)+" is running vulnerable FTP Version "+str(ans)
	except Exception, e:
		print "[+]Error="+str(e)

def main():
	ip1='10.10.50.67' #cmp ip_S
	ip2='10.10.35.45' #cmp ip_A:
	port=21
	establish(ip1,port)
	establish(ip2,port)

if __name__=='__main__':
	main()
	
