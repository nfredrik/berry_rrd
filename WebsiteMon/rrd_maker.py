#!/usr/bin/env python
import rrd

interval = 10
rrd_file = 'test.rrd'

my_rrd = rrd.RRD(rrd_file, vertical_label='value')
my_rrd.create_rrd(interval)