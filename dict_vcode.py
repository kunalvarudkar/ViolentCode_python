#dictionary from vcode3
#vcode3
#coded by-> Payload
services={'ftp':21,'ssh':22,'smtp':25,'http':80}
print services.keys()
print services.items()
services.has_key('ftp')
print services['ftp']
print "[+]Found vuln with FTP on port "+str(services['ftp'])

