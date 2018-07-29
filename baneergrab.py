import optparse
from socket import *
from threading import *
#semaphore provide a lock to threads from procedding i.e early execution.
screenlock=Semaphore(value=1)

def optparser():
    parser=optparse.OptionParser("Program usage -H <target host> -P <target port>")
    parser.add_option('-H',dest='tgthost',type='string',help='specify target host')
    parser.add_option('-P',dest='tgtport',type='string',help='specify target port[s]')
    (options,args)=parser.parse_args()
    tgthost=options.tgthost
    tgtport = str(options.tgtport).split(',')  
    if(tgthost==None)|(tgtport[0]==None):
        print parser.usage
        exit(0)
    for tp in tgtport:
        #we use thread to make our prog's execution faster.
        t=Thread(target=connscan,args=(tgthost,int(tp)))
        t.start()


def connscan(tgthost,tgtport):
    try:
        cons=socket(AF_INET,SOCK_STREAM)
        cons.connect((tgthost,tgtport))
        cons.send('violentdata')
        result=cons.recv(100)
        #using screenlock.acquire() we will hold the the thread until the semaphore release the thread lock
        screenlock.acquire()
        
        print "[+]Tcp port:"+str(tgtport)+" open"
        print "[+]Running service with version:"+str(result)
        cons.close()
    except Exception , e:
        screenlock.acquire()
        print "IP:"+str(tgthost)+" having:"+str(e)
    finally:
        #release the thread lock here
        screenlock.release()
        cons.close()

def main():
    optparser()

if __name__=='__main__':
    main()
