#code for taking parameter at command line
#coded by -> payload

import sys
if len(sys.argv)==2:   #sys.argv[0] contain info about python interpreter so if you want to except
#one parameter you should use argv value to two(2)
	filename=sys.argv[1] 
	print filename
