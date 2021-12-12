import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import shutil
import os

def sendmail(reciever_email):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email="shashwatesht.development@gmail.com"
    password = "9002748769"
    msg = MIMEMultipart()
    msg['from'] = sender_email
    msg['to'] = reciever_email
    msg['Subject'] = "Attendance issue"
    body = """ YOUR wards ATTENDANCE is below 50% please ask him to attend the LECTURES or else your ward will be detained. """
    msg.attach(MIMEText(body,'plain'))

    server=smtplib.SMTP(smtp_server,port)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender_email,password)
    server.sendmail(sender_email,reciever_email,msg.as_string())
    server.quit()

