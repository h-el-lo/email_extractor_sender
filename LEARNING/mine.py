import smtplib, datetime

server = 'localhost'
port = 1025

sender = 'thisliny@gmail.com'
reciever_list = [
    'dieufidel88@gmail.com',
    'andyonyeka101@gmail.com',
    'thisvane@gmail.com'
]


mail = smtplib.SMTP(server, port)
message = '%s \n%s \nHello mail world!\n- ' %(sender, reciever_list) + str(datetime.datetime.now())
mail.sendmail(sender, reciever_list, message)
mail.quit()