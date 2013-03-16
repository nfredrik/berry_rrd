#!/usr/bin/env python
import rrd
import time
import httplib
from bahnhof import bahnHof

# Todo: add logging feature, add mail everytime ftp is sent

host = 'www.kaj63.se'
path = '/'
use_ssl = False

interval = 10
rrd_file = 'test.rrd'

report_interval = 60 * 60            
            
def main():           
    bahnhof = bahnHof()
    report_time = time.time() + report_interval
     
    my_rrd = rrd.RRD(rrd_file, 'Response Time')
    while True:   
        start_time = time.time()
        if send(host):
            end_time = time.time()
            raw_latency = end_time - start_time
            expire_time = (interval - raw_latency)
            latency = ('%.3f' % raw_latency)
            my_rrd.update(latency)
            my_rrd.graph(60)
            print latency
        else:
            expire_time = interval
        if expire_time > 0:
            time.sleep(expire_time)
                
                
        if report_time < start_time:
            
            report_time = time.time() + report_interval
            bahnhof.upload('index.html')
            bahnhof.upload('test.rrd.png')  
            
           
def send(host):
    if use_ssl:
        conn = httplib.HTTPSConnection(host)
    else:
        conn = httplib.HTTPConnection(host)
    try:
        conn.request('GET', path)
        body = conn.getresponse().read()
        return True
    except:
        print 'Failed request'
        return False
        
        
if __name__ == '__main__':
    try:
        main()
    except:

        

           