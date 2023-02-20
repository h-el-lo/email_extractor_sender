* The software extracts emails from text files (with the email_extractor file) and sends bulk email to every email pushed to it (with either the sender.py file of tester(local).py file)
* Run the 'tester(local).py' to print messages to terminal using the command:
*   python -m smtpd -c DebuggingServer -n localhost:1025
* Run the 'sender.py' file to send the email through 'smtp.gmail.com'.
* Reconfigure the sender email in the 'sender' variable.
* Configure the body of the email in the 'body' variable
* For a gmail address, it is necessary to enable two-step-verification since 'less-secure-apps' enable/disable is no longer available in gmail. 
* Configure the email address as directed in the webpage below.
*   Handling the smtp.gmail.com api. https://towardsdatascience.com/how-to-easily-automate-emails-with-python-8b476045c151.