#!/usr/bin/env python
import rrd
import time
import httplib
import logging
import logging.handlers
from bahnhof import bahnHof

# Todo: add logging feature, add mail everytime ftp is sent

host = 'www.kaj63.se'
path = '/'
use_ssl = False

interval = 10
rrd_file = 'test.rrd'

report_interval = 60             
            
def main():

    LOG_FILENAME = 'rrdlogger'
    
    my_logger = logging.getLogger('rrdLogger')
    my_logger.setLevel(logging.DEBUG)
                        
    handler = logging.handlers.RotatingFileHandler(LOG_FILENAME,
                                               maxBytes=2048,
                                               backupCount=5,
                                               )
    my_logger.addHandler(handler)    
               
    bahnhof = bahnHof()
    
    report_time = time.time() + report_interval
    my_logger.debug('Log initiated')
     
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
            my_logger.debug('latency: %f'% latency)

        else:
            expire_time = interval
            my_logger.debug('No response from site?')
        if expire_time > 0:
            time.sleep(expire_time)
                
                
        if report_time < start_time:
            
            report_time = time.time() + report_interval
            try:
                bahnhof.upload('index.html')
                bahnhof.upload('test.rrd.png')  
                my_logger.debug('uploaded the suff')
                my_logger.info('Uploaded info...')
            except:
                my_logger.debug('failed to upload the suff')              
           
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
        return False
        
        
if __name__ == '__main__':
    main()

        

           