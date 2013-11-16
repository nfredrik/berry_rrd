#!/usr/bin/python -tt

import os
import sys
import time
import shutil

def main(args):

    try:
        os.remove('test.txt')
        os.remove('test2.txt')
    except:
        pass
    
    # Create file with random data
    nisse = open('test.txt', 'w')
    for i in range(10000):
        nisse.write(str(i))
        
    nisse.close()
    
    # Do some I/O-work for a while
    max_time =60
    start_time = time.time()  # remember when we started
    while (time.time() - start_time) < max_time:
        nisse2 = open('test2.txt', 'w')
        nisse = open('test.txt', 'r')
        while ("" != nisse.readline()):
        # for row in nisse.read():
            # print row
            nisse2.write('hello')
       
        nisse.close()
        nisse2.close()
    
    
    print 'the end'
    

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:] or 0))
