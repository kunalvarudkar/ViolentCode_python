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
