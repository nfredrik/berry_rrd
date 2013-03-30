from BeautifulSoup import BeautifulSoup
import urllib2

# Constants

#OMX_20130329=375.35
OMX_20130329=385.35
DIDNER_SVERIGE_20130229=1455.04
RELATION_OMX_DIDNER_20130229=DIDNER_SVERIGE_20130229/OMX_20130329

OMX_YESTERDAY=300.35
DIDNER_SVERIGE_YESTERDAY=1450.04
RELATION_OMX_DIDNER_YESTERDAY=DIDNER_SVERIGE_YESTERDAY/OMX_YESTERDAY

sample = list()

dgstor = "http://morningstar.se/Funds/Quicktake/Overview.aspx?perfid=0P00000F01&programid=0000000000"
# dgliten ="http://morningstar.se/Funds/Quicktake/Overview.aspx?perfid=0P0000IWH7&programid=0000000000"

sample.append(dgstor)
#sample.append(dgliten)
#url="http://morningstar.se/Funds/Quicktake/Overview.aspx?perfid=0P00000F01&programid=0000000000"

for d in sample:
    page=urllib2.urlopen(d)
    soup = BeautifulSoup(page.read())
    #print soup.prettify()
    didner=soup.find("table", {"class" : "alternatedtoplist halftoplist"})
    #print didner
    didner_kurs = didner.findAll('td')[1].text.replace(' ','').replace(',','.').replace('SEK','')
    print type(didner_kurs)
    didner_float = float(didner_kurs)
    print didner_float

#  <span class="Y DH"> </span><span class="Y DH">OMX STOCKHOLM (13:00)   375.35  +0.67 </span>

page=urllib2.urlopen("http://svt.se/svttext/web/pages/202.html")
soup = BeautifulSoup(page.read())
#print soup.prettify()
OMX=soup.findAll("span", {"class" : "Y DH"})
import re

#print OMX[1].text

filter = re.search(r"([\d]+\.[\d]+)", OMX[1].text) 

if filter != None:
    print 'OMX:', filter.group(0)
    omx_now = float(filter.group(0))
    
    
print 'Difference from 2013039:%.2f'%(((didner_float/omx_now/RELATION_OMX_DIDNER_20130229)-1)*100),'%'


print 'Difference from yesterday:%.2f'%(((didner_float/omx_now/RELATION_OMX_DIDNER_YESTERDAY)-1)*100),'%'


# 