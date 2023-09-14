
#=============================================================================
#=============================================================================
#=============================================================================


# This file was created to send bulk emails with attachments.
# It would read any file and extract any correctly structured email addresses found in it using the 'file_read' method.
# This script uses the 'smtp.gmail.com' server.
# The sender gmail account has to be configured accordingly: having 'two-step-verification' enabled. Steps for proper configuration are explained in the link below.
#           https://towardsdatascience.com/how-to-easily-automate-emails-with-python-8b476045c151.
# Add the email file to the directory of this file. Also ensure to add the file extension.
# The actual message of the email can be edited in the 'body' variable.

from email_extractor import read_file
import smtplib, ssl
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart


server = 'localhost'
port = 1025
user = input('Sender Email: ').strip()
password = input('\nEnter your email password and press enter: ').strip()
context = ssl.create_default_context()


snm = '''
==================================================
==================================================
Ensure to add both a first name and a last name with a space in-between!
Failure to do this will result in only the email address mane displaying as the sender.
Type the sender name in the desired alphabet case you wish to show.\nE.g, type "First User" or "FIRST USER".
These will output two different texts as the sender name.
==================================================
==================================================
'''


def create_message(receiver, body):
    global sender_name
    message = EmailMessage()
    message['From'] = sender_name
    message['Subject'] = 'Test mail'
    message['To'] = receiver
    message.set_content(body)

    return message


def get_mail_list():
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
    return addresses



with smtplib.SMTP(server, port) as mail:
    addresses = get_mail_list()
    # For the sender name to show, ensure to add a first name and a last name.
    # Failure to do this will result in only the email address mane displaying as the sender
    print(snm)
    sender_name = input('Sender Name: ').strip()
    body = '''After about twelve hours of work and research, debugging and the help of God, it is safe to say that this application is complete.
On this note, we'll like to appreciate you for your trust in us, and all the support you've given.'''
    # message = create_message(receiver, body)

    for receiver in addresses:
        message = create_message(receiver, body)
        mail.sendmail(user, receiver, message.as_string())



# DONE