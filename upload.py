from pyrrd.graph import DEF, CDEF, VDEF, LINE, AREA, GPRINT

from bahnhof import bahnHof

import sys
import os
import pickle

FILE='cobolmodules.pkl'

def from_file():

    if not os.path.exists(FILE):
        return {}

    pkl_file = open(FILE, 'rb')
    the_dict = pickle.load(pkl_file)
    pkl_file.close()
    return the_dict

def rrd_stuff():
        
    filename = 'test.rrd'
    
    #dataSource = from_file()
    
    
    #def1 = DEF(rrdfile=filename, vname='myspeed',
    #          dsName=dataSource.name)
    def1 = DEF(rrdfile=filename, vname='myspeed',
              dsName='speed')
    
    cdef1 = CDEF(vname='kmh', rpn='%s,3600,*' % def1.vname)
    cdef2 = CDEF(vname='fast', rpn='kmh,100,GT,kmh,0,IF')
    cdef3 = CDEF(vname='good', rpn='kmh,100,GT,0,kmh,IF')
    vdef1 = VDEF(vname='mymax', rpn='%s,MAXIMUM' % def1.vname)
    vdef2 = VDEF(vname='myavg', rpn='%s,AVERAGE' % def1.vname)
    
    line1 = LINE(value=100, color='#990000', legend='Maximum Allowed')
    area1 = AREA(defObj=cdef3, color='#006600', legend='Good Speed')
    area2 = AREA(defObj=cdef2, color='#CC6633', legend='Too Fast')
    line2 = LINE(defObj=vdef2, color='#000099', legend='My Average',
                 stack=True)
    gprint1 = GPRINT(vdef2, '%6.2lf kph')
    
    
    from pyrrd.graph import ColorAttributes
    ca = ColorAttributes()
    ca.back = '#333333'
    ca.canvas = '#333333'
    ca.shadea = '#000000'
    ca.shadeb = '#111111'
    ca.mgrid = '#CCCCCC'
    ca.axis = '#FFFFFF'
    ca.frame = '#AAAAAA'
    ca.font = '#FFFFFF'
    ca.arrow = '#FFFFFF'
    
    from pyrrd.graph import Graph
    graphfile = "rrdgraph.png"
    g = Graph(graphfile, start=920805000, end=920810000,
             vertical_label='km/h', color=ca)
    g.data.extend([def1, cdef1, cdef2, cdef3, vdef1, vdef2, line1, area1,
                   area2, line2, gprint1])
    g.write()




def main(args):

    rrd_stuff()
    
    try:
        bahnhof = bahnHof()
        bahnhof.upload('index.html')
        bahnhof.upload('rrdgraph.png')
        
    except:
        (exc_class, exc_object, exc_traceback) = sys.exc_info()
        print"""internal and completely unexpected problem, manifested as %s""" % str(exc_class)
            

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
  