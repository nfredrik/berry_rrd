from BeautifulSoup import BeautifulSoup
import urllib2
url="http://morningstar.se/Funds/Quicktake/Overview.aspx?perfid=0P00000F01&programid=0000000000"
page=urllib2.urlopen(url)
#print page.read()
soup = BeautifulSoup(page.read())
universities=soup.findAll('table',{'class':'"alternatedtoplist halftoplist'})
#universities=soup.findAll('a',class_='institution')
#universities=soup.findAll('A',{'CLASS':'institution'})
print universities

