=========== NEW THINGNS LEARNED ===========
* The smtpd package has been deprecated since Python 3.9. The third party aiosmtpd package is the recommended replacement. The equivalent command is "python -m aiosmtpd -n -l localhost:1025". https://stackoverflow.com/questions/55036268/sending-email-in-python-mimemultipart#55078292.\
* The aiosmtpd server stops quicker than an smtpd server.




=========== IMPROVEMENTS MADE ===========
* The 'tester(local).py' file sends email with the MIMEMultipart() objects.
* The sender name is specified as input when the program runs instead of having to edit the variable in the program.
* The sender email is specified as input when the program runs instead of having to edit the variable in the program.
* The sender.py file uses the email.mime module to create the email messages.
* Attachments can be added to text or html messages using the email.mime module