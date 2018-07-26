import optparse
from socket import *

'''def optparser():
	parser=optparse.OptionParser('Program Usage: Program_name.py --TH <Target Host> --TP <Target Port>')
	parser.add_option('--TH',dest='tgtHost',type='string',help='Specify Target Address')
	parser.add_option('--TP',dest='tgtPort',type='int',help='Specify Target port')
	(options,args)=parser.parse_args()
	tgthost=options.tgtHost
	tgtport=options.tgtPort
	if(tgthost==None) | (tgtport==None):
		print parser.usage
		exit(0)
	#connscan(tgthost,tgtport)
	#portscan(tgthost,tgtport) '''

def connscan(tgthost,tgtport):
	try:
		connS=socket(AF_INET,SOCK_STREAM)
		connS.connect((tgthost,tgtport))
		print "[+]TCP Port Open:"+str(tgtport)
		#connS.shutdown(socket.SHUT_RDWR)
		connS.close()
	except Exception, e:
		print e

def portscan(tgthost,tgtport):
	try:
		tgtip=socket.gethostbyname(str(gthost))
	except:
		print "[-]Cannot resolve '%s' : unknow host"%tgthost
		return
	try:
		tgtname=socket.gethostbyaddr(tgtip)
		print "[+] Printing result for: "+str(tgtname)[0]
	except:
		print "[+]Printing result for: "+str(tgtip)
	setdefaulttimeout(2)


def main():
	#optparser()
	parser=optparse.OptionParser('Program Usage: Program_name.py -H <Target Host> -TP <Target Port>')
        parser.add_option('-H',dest='tgtHost',type='string',help='Specify Target Address')
        parser.add_option('-P',dest='tgtPort',type='int',help='Specify Target port')
        (options,args)=parser.parse_args()
        tgthost=options.tgtHost
        tgtport=options.tgtPort
        if(tgthost==None) | (tgtport==None):
                print parser.usage
                exit(0)
	
	connscan(tgthost,tgtport)
	portscan(tgthost,tgtport)
	

if __name__=='__main__':
	main()

