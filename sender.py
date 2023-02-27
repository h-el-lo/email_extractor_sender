# This file was created to send multiple multiple simple text mails to different email addresses.
# It would read any file and extract any correctly structured email addresses found in it using the 'file_read' method.
# This script is capable of sending bulk text email containing a title and a body using the 'smtp.gmail.com' server.
# The sender gmail account has to be configured accordingly: having 'two-step-verification' enabled. Steps for proper configuration are explained in the link below.
#           https://towardsdatascience.com/how-to-easily-automate-emails-with-python-8b476045c151.
# Add the email file to the directory of this file. Also ensure to add the file extension.
# The actual message of the email can be edited in the 'body' variable.

from email_extractor import read_file
import smtplib, ssl
from email.message import EmailMessage

server = 'smtp.gmail.com'
port = 465
user = str(input('Sender Email: ')).strip()        
password = input('\nEnter your email password and press enter: ').strip()


body = '''After about twelve hours of work and research, debugging and the help of God, it is safe to say that this application is complete.
On this note, we'll like to appreciate you for your trust in us, and all the support you've given.'''


message = EmailMessage()

print('\n')
print('='*50)
print('='*50)
print('Ensure to add both a first name and a last name with a space in-between!')
print('Failure to do this will result in only the email address mane displaying as the sender.')
print('Type the sender name in the desired alphabet case you wish to show.\nE.g, type "First User" or "FIRST USER".')
print('These will output two different texts as the sender name.')
print('='*50)
print('='*50)
print('\n')

# For the sender name to show, ensure to add a first name and a last name.
# Failure to do this will result in only the email address mane displaying as the sender
sender_name = input('Sender Name: ').strip()


def create_message(receiver):
    global sender_name, body
    message = EmailMessage()
    message['From'] = sender_name
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

context = ssl.create_default_context()
with smtplib.SMTP_SSL(server, port, context=context) as mail:

    mail.login(user, password)

    for receiver in addresses:
        message = create_message(receiver)
        mail.sendmail(user, receiver, message.as_string())

# Ensure to maintain a stable internet connection throughout the process.