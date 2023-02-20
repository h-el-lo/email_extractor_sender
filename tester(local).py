# This file was created to send multiple multiple simple text mails to different email addresses.
# It would read any file and extract any correctly structured email addresses found in it using the 'file_read' method.
# This file will output the messages on a debugging server, not an actual online server.
# To activate the server in a terminal, run the command
#       python -m smtpd -c DebuggingServer -n localhost:1025
# smtpd (simple mail transter protocol debugging) server
# Add the email file to the directory of this file. Also ensure to add the file extension.
# Ensure to change the 'sender' variable to the desired sender email address.

from email_extractor import read_file
import smtplib, datetime

server = 'localhost'
port = 1025

# CHANGE THE SENDER VARIABLE. ENSURE TO LEAVE THE SENDER EMAIL IN WITHIN THE QUOTES. E.g 'sender@email.com'.
sender = 'myemail@gmail.com'

def create_message(reciever, time):

    global sender
    message = '''From: %s
To: %s
Subject: Test mail
Message: Not so new to sending multiple emails on local smtpd servers.
- %s''' %(sender, reciever, time)

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

with smtplib.SMTP(server, port) as mail:
    for reciever in addresses:
        message = create_message(reciever, str(datetime.datetime.now()))
        mail.sendmail(sender, reciever, message)

    