from BeautifulSoup import BeautifulSoup
import urllib2
url="http://www.utexas.edu/world/univ/alpha/"
page=urllib2.urlopen(url)
#print page.read()
soup = BeautifulSoup(page.read())
universities=soup.findAll('a',{'class':'institution'})
#universities=soup.findAll('a',class_='institution')
#universities=soup.findAll('A',{'CLASS':'institution'})
for eachuniversity in universities:
    print eachuniversity['href']+","+eachuniversity.string
