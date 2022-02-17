import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def mail(word):
    mail_content = '''Subject: WARNING! FLAGGED WORD USED!
                    WORD USED: '''+word
    print(mail_content)
    sender_address = 'keysafe2021@gmail.com'
    sender_pass = 'PES2021internship'
    receiver_address = 'anishsurendra7@gmail.com'
    message = MIMEMultipart()
    message['From']=sender_address
    message['To']=receiver_address
    message['Subject'] = 'A test mail sent by Python. It has an attachment.' 
    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587) 
    session.starttls() 
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')