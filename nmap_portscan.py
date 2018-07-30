# Port scanning code using Nmap package
#code by -> payload

import nmap
import optparse
from socket import *
def nmapscan(tgtip,port):
	try:
                nmscan=nmap.PortScanner()
                nmscan.scan(tgtip,port)
                state=nmscan[tgtip]['tcp'][int(port)]['state']
		try:
			connSkt = socket(AF_INET, SOCK_STREAM)
			connSkt.connect((tgtip, int(port)))
			results = connSkt.recv(100)
			print "[*]" + tgtip + " tcp/"+port +" "+state+" "+str(results)
		except Exception ,e :
			print "[-]Facing error:"+str(e)

	except Exception,e:
                print "Cant scan IP"+str(e)+" for port:"+str(port)+" either the ip is not rechable or no service is running" 
                return


def main():
	parse=optparse.OptionParser("Program Usage -H <Target IP> -P <Target port[s]>")
	parse.add_option('-H',dest='tgtip',type='string',help='Specify target ip')
	parse.add_option('-P',dest='ports',type='string',help='Specify ports spearated by commas (,)')
	(options,args)=parse.parse_args()
	tgtip=options.tgtip
	ports=str(options.ports).split(',')
	if(tgtip==None)|(ports[0]==None):
		print parse.usage
		exit(0)
	print "[!]Scanning ports using NMAP[!]" 
	for port in ports:
		nmapscan(tgtip,port)
	print "[-]Stopping Scan[-]"
	#nmapscan()

if __name__=='__main__':
	main()
