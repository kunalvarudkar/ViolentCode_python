#Small tool for dictionary based attack
#coded by -> payload
#code require two file 
	#1)Hash file with password as plaintext and in hash format  --- filename = demo_hash_pass.txt
	#2)/etc/shadow                                              --- filename = demoshadow.txt
#note:- this the file which i have used uses crypt() from python with max salt value of 2
# /etc/shadow may use diff hashing algo which may differ from the one i have used.



def readshadow():
	shadow=open('demoshadow.txt','r')
	line=shadow.readline()
	while line:
		data=line.strip()
		if ":" in data:
			user=line.split(':')[0]
			hashpass=line.split(':')[1]
			#print "******"
			#print user
			#print "in readshadow->"+str(hashpass)
			gethashfile(hashpass)
		line=shadow.readline()
	shadow.close()
	


def gethashfile(cmphash):
	#print "in gethashfile->"+str(cmphash)
	hashfile=open('demo_hash_pass.txt','r')
	line=hashfile.readline()
	while line:
		data=line.strip()
		if ":" in data:
			user=line.split(':')[0]
			password=line.split(':')[1]
			hashpass=line.split(':')[2].strip(' ')
			if(hashpass==cmphash):
				print "[+]FOUND[+]"
				print "[+]USERNAME="+str(user)+" PASSWORD="+str(password)+" CRYPTPASS="+str(hashpass)
		line=hashfile.readline() 
	hashfile.close()
	

def main():
	readshadow()	

if __name__=='__main__':
	main()
