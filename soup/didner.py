import smtplib
import email.utils
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass

class Mail(object):

    def __init__(self, to, username, password, servername):
        self.to_email = to
        self.username = username
        self.password = password
        self.server = smtplib.SMTP(servername, 587)

    def send(self, subject, message, attach=[]):
        # Create message 
        msg = MIMEMultipart()
        msg.set_unixfrom('author')
        msg['To'] = email.utils.formataddr(('Recipient', self.to_email))
        msg['From'] = email.utils.formataddr(('Author', 'author@example.com'))
        msg['Subject'] = subject
        msg.attach( MIMEText(message) )
        
        try:
            self.server.set_debuglevel(False)

            # identify ourselves, prompting server for supported features
            self.server.ehlo()

           # If we can encrypt this session, do it
            if self.server.has_extn('STARTTLS'):
                self.server.starttls()
                self.server.ehlo() # re-identify ourselves over TLS connection

            # Attach files, if we have anything
            for atta in attach:
                part = MIMEBase('application', "octet-stream")
                part.set_payload( open(atta,"rb").read() )
                Encoders.encode_base64(part)
                part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(atta))
                msg.attach(part)


            self.server.login(self.username, self.password)
            self.server.sendmail('author@example.com', [self.to_email], msg.as_string())
        finally:
            self.server.quit()



from BeautifulSoup import BeautifulSoup


import urllib2
import json
import pickle
import os
import re

# Constants
FILE='yesterday.pickle'
OMX_20130329=375.35
DIDNER_SVERIGE_20130229=1455.04
RELATION_OMX_DIDNER_20130229=DIDNER_SVERIGE_20130229/OMX_20130329


# Save values from today
def write_2_file(dict):
    
    output = open(FILE, 'wb')
    # Save with new protocol i.e -1
    pickle.dump(dict, output, -1)
    output.close()

# Read values from yesterday
def from_file():

    if not os.path.exists(FILE):
        return {}

    pkl_file = open(FILE, 'rb')
    the_dict = pickle.load(pkl_file)
    pkl_file.close()
    return the_dict

obj = {}

if os.path.exists(FILE):
    obj = from_file()
else:
    print type(obj)
    obj['OMX_YESTERDAY'] = 380.35
    obj['DIDNER_SVERIGE_YESTERDAY'] = 1451.04
    write_2_file(obj)
    
    
RELATION_OMX_DIDNER_YESTERDAY = obj['DIDNER_SVERIGE_YESTERDAY']/obj['OMX_YESTERDAY']

dgstor = "http://morningstar.se/Funds/Quicktake/Overview.aspx?perfid=0P00000F01&programid=0000000000"
# dgliten ="0P0000IWH7"


sum= ""
sum+='-'*50 +'\n'
sum+="Didner yesterday:%.2f"%obj['DIDNER_SVERIGE_YESTERDAY']+'\n'
sum+="OMX yesterday:%.2f"%obj['OMX_YESTERDAY']+'\n'



#
# Read OMX from text-TV
#

#  <span class="Y DH"> </span><span class="Y DH">OMX STOCKHOLM (13:00)   375.35  +0.67 </span>

page=urllib2.urlopen("http://svt.se/svttext/web/pages/202.html")
soup = BeautifulSoup(page.read())
OMX=soup.findAll("span", {"class" : "C DH"})

# print 'OMX:', OMX

filter = re.search(r"([\d]+\.[\d]+)", OMX[1].text) 
if filter != None:
    omx_now = float(filter.group(0))

#
#  Read didner & gerge from morningstar
#

page=urllib2.urlopen(dgstor)
soup = BeautifulSoup(page.read())
#print soup.prettify()
didner=soup.find("table", {"class" : "alternatedtoplist halftoplist"})
didner_float = float(didner.findAll('td')[1].text.replace(' ','').replace(',','.').replace('SEK',''))


sum+='-'*50 +'\n'
sum+="Didner course today: %.2f\n"% didner_float
sum+="OMX today: %.2f\n"% omx_now    
#print 'Difference from 2013039: %.2f'%(((didner_float/omx_now/RELATION_OMX_DIDNER_20130229)-1)*100),'%'
sum+='Didner compared to OMX from 20130329: %.2f'%(((didner_float/omx_now/RELATION_OMX_DIDNER_20130229)-1)*100) + '%\n'
sum+= 'Didner compared to OMX from yesterday:%.2f'%(((didner_float/omx_now/RELATION_OMX_DIDNER_YESTERDAY)-1)*100)+'%\n'


#
# Save todays metrics
#
obj['OMX_YESTERDAY'] = omx_now
obj['DIDNER_SVERIGE_YESTERDAY'] = didner_float

write_2_file(obj)


#print '---Printing sum---'
# print sum

mail = Mail('fredrik.svard@gmail.com', 'frsv.linux@gmail.com', 'hoppa2lo', 'smtp.gmail.com')  
mail.send('Didner och OMX', sum,[])