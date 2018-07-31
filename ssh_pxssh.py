from pexpect import pxssh
#import pexpect
def send_cmd(s,cmd):
	s.sendline(cmd)
	s.prompt()
	print s.before

def connect(host,user,password):
	try:
		s=pxssh.pxssh()
		s.login(host,user,password)
		return s
	except:
		print "[-]Error connecting"

def main():
	s=connect('127.0.0.1','kpit','haha123')
	send_cmd(s,'uname -a & whoami ')
        #pexpect.expect('password:')
	#pexpect.sendline('haha123')
if __name__=='__main__':
	main()
