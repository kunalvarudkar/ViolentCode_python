#sample program for string handeling and its method
#vcode1
#Coded by-> Payload

port=21
baneer="FreeFloat FTP server"
print "[+]Checking for "+baneer+" on port "+str(port)
print(type(baneer))
portlist=[80,443,21]
print(type(portlist))
portopen=True
print (type(portopen))
print baneer.upper()
print baneer.lower()
print baneer.replace('FreeFloat','Ability')
print baneer.find('FTP')

#list form vcode2

portlist=[]
portlist.append(21)
portlist.append(80)
portlist.append(443)
portlist.append(25)
print portlist
portlist.sort() #first do sorting
print portlist #then print !!
pos = portlist.index(80)
print "[+]There are "+str(pos)+" ports to scan before 80."
portlist.remove(443)
print portlist
cnt = len(portlist)
print "[+]Scanning "+str(cnt)+" Total ports"

#dictionary from vcode3

services={'ftp':21,'ssh':22,'smtp':25,'http':80}
print services.keys()
print services.items()
services.has_key('ftp')
print services['ftp']
print "[+]Found vuln with FTP on port "+str(services['ftp'])








