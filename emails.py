
#!/usr/bin/env python3
from email.message import EmailMessage
import os
import mimetypes
import smtplib

def generate_email(From,To,SubjectLine,EmailBody,Attachement):
   message = EmailMessage()
   message['From'] = From
   message['To'] = To
   message['Subject'] = SubjectLine
   message.set_content(EmailBody)
   filename = os.path.basename(Attachement)
   print(filename)
   mime_type,_ = mimetypes.guess_type(filename)
   mime_type,mime_sub_type = mime_type.split('/',1)
   print(mime_type,",",mime_sub_type)
   with open(Attachement,'rb') as attach:
       message.add_attachment(attach.read(),
                              maintype = mime_type,
                              subtype = mime_sub_type,
                              filename = os.path.basename(Attachement)
                             )
   return message



def generate_health_check_email(From,To,SubjectLine,EmailBody):
   message = EmailMessage()
   message['From'] = From
   message['To'] = To
   message['Subject'] = SubjectLine
   message.set_content(EmailBody)
   return message



def send_email(message):
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()
