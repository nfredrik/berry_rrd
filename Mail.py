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

    def send(self, msg):
        # Create message 
        msg = MIMEText('Test message from PyMOTW.')
        msg.set_unixfrom('author')
        msg['To'] = email.utils.formataddr(('Recipient', self.to_email))
        msg['From'] = email.utils.formataddr(('Author', 'author@example.com'))
        msg['Subject'] = 'Test from PyMOTW'

        try:
            self.server.set_debuglevel(True)

            # identify ourselves, prompting server for supported features
            self.server.ehlo()

           # If we can encrypt this session, do it
            if self.server.has_extn('STARTTLS'):
                self.server.starttls()
                self.server.ehlo() # re-identify ourselves over TLS connection

            self.server.login(self.username, self.password)
            self.server.sendmail('author@example.com', [self.to_email], msg.as_string())
        finally:
            self.server.quit()

