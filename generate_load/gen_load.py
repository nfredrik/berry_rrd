#!/usr/bin/python -tt


import sys
import time

def main(args):


    # Create file with random data
    nisse = open('test.txt', 'w')
    for i in range(10000):
        nisse.write(str(i))
        
    nisse.close()
    
    # Do some I/O-work for a while
    max_time =5
    start_time = time.time()  # remember when we started
    while (time.time() - start_time) < max_time:
        nisse = open('test.txt', 'r')
        for row in nisse.read():
            print row
       
        nisse.close()
    
    
    print 'the end'
    

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:] or 0))
