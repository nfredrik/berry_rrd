import sys
from ftplib import FTP

# http://privat.bahnhof.se/wb177225/


class myFTP(object):
    
    def __init__(self, site, usr, pwd):
        # self.ftp = fille(site)        
        print 'init'
        self.ftp =  FTP(site)
        self.ftp.login(user=usr, passwd=pwd)

    def upload(self, file):
        print 'upload'
        self.ftp.storbinary('STOR ' + file, open(file, 'rb'))
        
    def __del__(self):
        #pass
        print 'del'
        self.ftp.quit()
        #print 'ftp session terminated' 
        

class bahnHof(object):
    def __init__(self):
        self.bahnhof = myFTP('privat.bahnhof.se', 'wb177225', '94e6a11d6')        

    def upload(self,file):
        self.bahnhof.upload(file)
        
        
def main(args):
    
 
    try:
        bahnhof = myFTP('privat.bahnhof.se', 'wb177225', '94e6a11d6')
        bahnhof.upload('index.html')
        bahnhof.upload('/tmp/ rrdgraph.png')
        
    except:
        (exc_class, exc_object, exc_traceback) = sys.exc_info()
        print"""internal and completely unexpected problem, manifested as %s""" % str(exc_class)
            
  
    

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
