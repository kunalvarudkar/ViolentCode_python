import zipfile
import os
import sys
import time
def bruteforce(filename,zfile):
	#zFile=zfile
	dic=open(filename,'r')
	line=dic.readline()
	while line:
		password=line.strip()
		#print password
		try:
			print "[!]Trying password -> "+str(password)
			zfile.extractall(pwd=password)
			print ("FOUND")
                        print ("[+]Password cracked ->"+str(password))
                        #exit(0)
		#line=dic.readline()
		
		except Exception , e:
			print "[-]NOT MATCHED[-]"
		line=dic.readline()
	dic.close()


def checkipfile():
	if len(sys.argv)==3:
		filename=sys.argv[1]
		zfile=sys.argv[2]
	if not os.path.isfile(filename):
		print "[-]File does not exist[-]"
	if not os.path.isfile(zfile):
		print "[-]File does not exist[-]"
	if not os.access(zfile,os.R_OK):
                print "[-]File dont have read access[-]"
	if not os.access(filename,os.R_OK):
		print "[-]File dont have read access[-]"
	#pwd=str(os.system('pwd'))
	#zfile=pwd+str(zfile)
	#print zfile
	#time.sleep(10)
	ZIPFILE = zipfile.ZipFile(zfile) #!! DAMN IMPORTANT!! -> else will create an [ERROR] "'str' object has no attribute 'extractall' "
	bruteforce(filename,ZIPFILE)

def main():
	checkipfile()

if __name__=='__main__':
	main() 
