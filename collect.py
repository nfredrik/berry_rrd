import os
import sys
import time
from pyrrd.rrd import DataSource,  RRA, RRD
import pickle

FILE='cobolmodules.pkl'

def write_2_file(dict):
    
    output = open(FILE, 'wb')
    # Save with new protocol i.e -1
    pickle.dump(dict, output, -1)
    output.close()
    
def from_file():

    if not os.path.exists(FILE):
        return {}

    pkl_file = open(FILE, 'rb')
    the_dict = pickle.load(pkl_file)
    pkl_file.close()
    return the_dict


def main(args):
    
    filename = 'test.rrd'
    
    
    if not os.path.exists(filename):
        dataSources = []
        roundRobinArchives = []
        
        dataSource = DataSource(dsName='speed', dsType='COUNTER', heartbeat=600)
        print "dataSource.name:" , dataSource.name
        dataSources.append(dataSource)
        
        roundRobinArchives.append(RRA(cf='AVERAGE', xff=0.5, steps=1, rows=24))
        roundRobinArchives.append(RRA(cf='AVERAGE', xff=0.5, steps=6, rows=10))
        
        myRRD = RRD(filename, ds=dataSources, rra=roundRobinArchives, start=920804400)
        myRRD.create()
        #myRRD.update()
        #write_2_file(myRRD)
    
    else:
        
        import random
        
        myRRD = RRD(filename)    
        myRRD.bufferValue(time.time(), random.randrange(12393, 12423))
        
        #=======================================================================
        # myRRD.bufferValue('920805900', '12363')
        # myRRD.bufferValue('920806200', '12373')
        # myRRD.bufferValue('920806500', '12383')
        # myRRD.update()
        # 
        # myRRD.bufferValue('920806800', '12393')
        # myRRD.bufferValue('920807100', '12399')
        # myRRD.bufferValue('920807400', '12405')
        # myRRD.bufferValue('920807700', '12411')
        # myRRD.bufferValue('920808000', '12415')
        # myRRD.bufferValue('920808300', '12420')
        # myRRD.bufferValue('920808600', '12422')
        # myRRD.bufferValue('920808900', '12423')
        #=======================================================================
        myRRD.update()
        
        #write_2_file(myRRD)

        print os.path.isfile(filename)
        print len(open(filename).read())



if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
    