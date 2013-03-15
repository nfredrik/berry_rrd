from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.Utils import COMMASPACE, formatdate
from email import Encoders

import os
import sys
import smtplib
import email.utils
from email.mime.text import MIMEText
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


def main(args):
    mail = Mail('fredrik.svard@gmail.com', 'frsv.linux@gmail.com', 'hoppa2lo', 'smtp.gmail.com')
    attachment = ['Mail.py'] 
    mail.send('from pi', 'http://privat.bahnhof.se/wb177225', attachment)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:] or 0))

