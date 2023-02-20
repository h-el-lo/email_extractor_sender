# This file was created to send multiple multiple simple text mails to different email addresses.
# It would read any file and extract any correctly structured email addresses found in it using the 'file_read' method.
# This script is capable of sending bulk text email containing a title and a body using the 'smtp.gmail.com' server.
# The sender gmail account has to be configured accordingly: having 'two-step-verification' enabled. Steps for proper configuration are explained in the link below.
#           https://towardsdatascience.com/how-to-easily-automate-emails-with-python-8b476045c151.
# Add the email file to the directory of this file. Also ensure to add the file extension.
# Ensure to change the 'sender' variable to the desired sender email address.
# The actual message of the email can be edited in the 'body' variable.

from email_extractor import read_file
import smtplib, ssl
from email.message import EmailMessage

server = 'smtp.gmail.com'
port = 465

# CHANGE THE SENDER VARIABLE. ENSURE TO LEAVE THE SENDER EMAIL IN WITHIN THE QUOTES. E.g 'sender@email.com'.
# Also, changes can be made to the body variable. However, ensure to leave the message within the triple quotes. E.g 
#    '''This is the changed message. The changes have been applied. However, the message is still within the triple quotes.'''
sender = 'thisliny@gmail.com'
password = input('\nEnter your email password and press enter: ').strip()
body = '''After about twelve hours of work and research, debugging and the help of God, it is safe to say that this application is complete.
On this note, we'll like to appreciate you for your trust in us, and all the support you've given.'''


message = EmailMessage()
message['From'] = sender



def create_message(receiver):
    global sender, body
    message = EmailMessage()
    message['From'] = sender
    message['Subject'] = 'Test mail'
    message['To'] = receiver
    message.set_content(body)

    return message



file_not_found = True
while file_not_found:
    email_file = input('\nEnter email file name (including file extension): ')

    try:
        addresses = read_file(email_file)
    except FileNotFoundError:
        print('File not found! Try again\n')
        continue
    break


del file_not_found
# Deletes the file_not_found variable
# addresses = ['dieufidel88@gmail.com', 'thisvane@gmail.com', 'soloetuh1919@gmail.com']

context = ssl.create_default_context()
with smtplib.SMTP_SSL(server, port, context=context) as mail:

    mail.login(sender, password)

    for receiver in addresses:
        message = create_message(receiver)
        mail.sendmail(sender, receiver, message.as_string())

# Ensure to maintain a stable internet connection throughout the process.