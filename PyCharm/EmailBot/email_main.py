import smtplib
from email.message import EmailMessage
from sys import argv
from string import Template
from pathlib import Path

reciever_email = ""
username = ""
password = ""
mail_server = ""
reciever_name = ""
subject = ""
content = ""

def getData():
    global reciever_email, mail_server, username, password
    try:
        reciever_email = argv[1]
        mail_server = argv[2]
        username = argv[3]
        password = argv[4]
    except Exception:
        print('Sorry please provide arguments'
              '\n<ReceiverEmail> <Mailserver> <SenderEmail> <Password> *<Reciever Name>* *<Subject>*'
              '\nExample of mailservers gmail.com, yahoo.com, live.com'
              '\nNote: Receiver Name and Subject are \033[1m' + 'optional')
        exit()


def getReceiverName():
    global reciever_name, reciever_email
    try:
        reciever_name = argv[5]
    except Exception:
        reciever_name = reciever_email


def getSubject():
    global subject
    try:
        subject = argv[6]
    except Exception:
        subject = "Hello"


def createEmail(username, reciever_name, reciever_email, subject, content):
    email = EmailMessage()
    email['from'] = username
    email['to'] = reciever_email
    email['subject'] = subject
    email.set_content(content.substitute({'r_name' : reciever_name}), 'html')
    return email


def sendEmail(reciever_email, reciever_name, subject, username, password, mail_server, content):
    with smtplib.SMTP(host=f'smtp.{mail_server}', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(str(username), str(password))
        smtp.send_message(createEmail(username, reciever_name, reciever_email, subject, content))
        print(f'email successfully sent from {str(mail_server)}')


getData()
getReceiverName()
getSubject()

content = Template(Path("email.html").read_text())
sendEmail(reciever_email, reciever_name, subject, username, password, mail_server, content)