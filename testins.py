from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl

server, port = 'localhost', 1025
context = ssl.create_default_context()
mail = SMTP(server, port)

message = MIMEMultipart('alternative')
message['From'] = 'vANqUisH ThE fOE'
message['To'] = 'reawstest@gmail.com'
message['Subject'] = 'The subject of the day.'

plain = '''
The king's message goes thus: Thou shalt be my slave
so shalt thou toil in my caves
till thy gray hair go down to thy grave
and then shalt thou be saved'''

html = '''\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.realpython.com">Real Python</a> 
       has many great tutorials.
    </p>
  </body>
</html>
'''

velon = MIMEText(plain, 'plain')
tratos = MIMEText(html, 'html')

message.attach(velon)
message.attach(tratos)


try:
    mail.sendmail('thisliny@gmail.com', 'reawstest@gmail.com', message.as_string())
    mail.close()
except Exception as e:
    print('Error occured: ', e)
finally:
    mail.close()

    # USING BASIC MULTIPART ALTERNATIVE CLASS