# Sending email modules
# make sure SMTP server is installed in local machine
# Host is SMTP server
# Port is 25
# this is a change

import smtplib
from email.message import EmailMessage

import socket
soc = socket.socket()
# host = socket.gethostname()
host = '192.168.0.26'
port = 25

print('connecting ', 'Host: ', host, 'Port: ', port)
soc.connect(('192.168.0.26', port))

e_mail = EmailMessage()

e_mail['Subject'] = 'Test file from Python testing'
e_mail['From'] = 'mohan.kris24@gmail.com'
e_mail['To'] = 'mohan.kris24@gmail.com'

s = smtplib.SMTP(host, port)
s.send_message(e_mail)
s.quit()
