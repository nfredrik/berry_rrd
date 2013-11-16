
#!/usr/bin/python -tt

import os
import sys
import time
import shutil

def main(args):

    
    # Do some I/O-work for a while
    max_time =60
    start_time = time.time()  # remember when we started
    while (time.time() - start_time) < max_time:
        nisse2 = open('file.txt', 'rb')
        nisse2.read()
        nisse2.close()
    
    
    print 'the end'
    

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:] or 0))
