#sample code for bruteforcing a zip file
#coded by -> pyload
import zipfile
import optparse
from threading import Thread 

def extractfile(zFile,password):
	try:
		zFile.extractall(pwd=password) #check if pwd==password
		print "[+]Password Found:" +str(password) 
	except Exception ,e:
		print "[-]ERROR Brute Forcing[-]"
		#print (e)


def main():
       # print usage instructions (1)
	parser=optparse.OptionParser("usage%prog "+\
	"-f <zipfile> -d <dictionary>")

	# defines the desired options for -f usage (2) 
	parser.add_option('-f',dest='zname', type='string', \
	help='specify zip file')
	
	# defines the desired options for -d usage (3)
	parser.add_option('-d',dest='dname',type='string',\
	help='Specify Dictionary file')
	
	# not sure but it does binding work of option & args with parse_args()
	(options,args)=parser.parse_args()

	# check if the input files are provided
	if(options.zname==None)|(options.dname==None):
		print parser.usage  #prints the usage of any one of the file is
					#missing
		exit(0)
	else:
		zname=options.zname  # else the zipfile name is stored on zname
		dname=options.dname	# same as above
	zFile=zipfile.ZipFile(zname)  #initialize the zame with zipfile package # and then save it to zFile 

	passfile=open(dname) # opens the file 
	for line in passfile.readlines(): # reads each line of the dict file
		password=line.strip('\n')  # storing each line in password
		
		# creating the thread and passing proper args to the target ()
		t=Thread(target=extractfile, args=(zFile,password)) 
		t.start() # starting the Thread

if __name__=='__main__':
	main() #calling main()
