import smtplib
import datetime

SERVER = 'localhost'
PORT = 1025

FROM = "me@mydevice.com"
TO = ["myemailaddress@something.com"]

SUBJECT = "test"

dt = datetime.datetime.now()
TEXT = "blabla bla \n@ " + str(dt)

message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ",".join(TO), SUBJECT, TEXT)

# server = smtplib.SMTP(SERVER, PORT)
# server.sendmail(FROM, TO, message)
# server.quit()

# In the following lines, the context manager is introduced so that the server object is quit and cleaned up after the with-as block.

with smtplib.SMTP(SERVER, PORT) as server:
    server.sendmail(FROM, TO, message)