#!/usr/bin/python -tt

import sys
from Mail import Mail


def main(args):
    mail = Mail('fredrik.svard@gmail.com', 'frsv.linux@gmail.com', 'hoppa2lo', 'smtp.gmail.com')
    
    mail.send('from pi', 'Sylvia Wrethammar',[])

 
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:] or 0))
