import os
import sys

if len(sys.argv)==2:
	filename=sys.argv[1]
	if not os.path.isfile(filename):
		print "[-]File does not exist[-]"
		exit(0)
	if not os.access(filename,os.R_OK):
		print "[-]Read permission denied[-]"
		exit(0)
	print "[+] Reading file= "+str(filename)
