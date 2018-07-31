# code for ssh login using python 
#note:- this code does not keey the ssh session live it terminates after executing the command
# coded by -> payload

#!/usr/bin/env python
import pexpect

def connect(user,host,password):
	ssh_newkey = 'Are you sure you want to continue connecting'
	# my ssh command line
	#child=pexpect.spawn('ssh kpit@10.10.51.71 uname -a')
	child=pexpect.spawn('ssh '+user+'@'+host+' uname -a')
	ret=child.expect([ssh_newkey,'password:',pexpect.EOF])
	print ret
	if ret==0:
		print "[!]Found: "+str(ssh_newkey)
		print "[!]On list[0]"
		print "sending input: yes"
		child.sendline('yes')
		ret=child.expect([ssh_newkey,'password:',pexpect.EOF])
	if ret==1:
		print "[-]Not found: "+str(ssh_newkey)
		print "[!]Jumping to List[1]"
		print "typing password to get ssh login",
    		child.sendline("qemu")
    		child.expect(pexpect.EOF)    
	elif ret==2:
    		print "Connection Timeout"
    		pass
	print child.before # print out the result

def main():
	user='demouser'
	password='haha123'
	host='10.10.1.100'
	connect(user,host,password)

if __name__=='__main__':
	main()
