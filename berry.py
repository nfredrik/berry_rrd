from pyrrd.rrd import DataSource, RRA, RRD
filename = '/tmp/test.rrd'
dataSources = []
roundRobinArchives = []
dataSource = DataSource(
dsName='speed', dsType='COUNTER', heartbeat=600)
dataSources.append(dataSource)
roundRobinArchives.append(RRA(cf='AVERAGE', xff=0.5, steps=1, rows=24))
roundRobinArchives.append(RRA(cf='AVERAGE', xff=0.5, steps=6, rows=10))
myRRD = RRD(
filename, ds=dataSources, rra=roundRobinArchives, start=920804400)
myRRD.create()