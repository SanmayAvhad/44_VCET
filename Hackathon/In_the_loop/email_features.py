
import os
import openai
from unittest import result
import schedule
import datetime
import smtplib
import mysql.connector  

from pickle import TRUE
from django.shortcuts import render
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
<<<<<<< HEAD
from email import encoders, message
=======
from email import encoders
import email
import imaplib
>>>>>>> 7d21bd9e4ebb7e195b35bae16345f8e33bc3697f


def receive_emails():

    N= 8 #Top 8 email to fetch

    EMAIL = 'jatintiwari123@outlook.com'
    PASSWORD = 'Jatin!@#$1'
    SERVER = 'outlook.office365.com'

    mail = imaplib.IMAP4_SSL(SERVER)
    mail.login(EMAIL, PASSWORD)
    mail.select('inbox')
    status, data = mail.search(None, 'ALL')
    mail_ids = []
    email_list = []
    print(len(mail_ids))
    for block in data:
        mail_ids += block.split()
    print(type(mail_ids))
    print(mail_ids)
    for i in mail_ids:
        status, data = mail.fetch(i, '(RFC822)')
        for response_part in data:
            if isinstance(response_part, tuple):
                message = email.message_from_bytes(response_part[1])
                mail_from = message['from']
                mail_subject = message['subject']
                if message.is_multipart():
                    mail_content = ''

                    for part in message.get_payload():
                        if part.get_content_type() == 'text/plain':
                            mail_content += part.get_payload()
                else:
                    mail_content = message.get_payload()
                print(f'From: {mail_from}')
                print(f'Subject: {mail_subject}')
                print(f'Content: {mail_content}')
                email_list.append([mail_from,mail_subject,mail_content]) 
    
        # print(type(email_list))
    email_list = email_list[::-1]
    # print(len(email_list))
    # for i in email_list:
    #     print(i)
    # case_list = []
    # for entry in email_list:
    #     case = {'sender': email_list[0][0], 'subject': email_list[0][1], 'body':email_list[0][2] }
    #     case_list.append(case.copy())
    
    return email_list






def openAI(title):



    openai.api_key ="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"


    response = openai.Completion.create(
    model="text-davinci-002",
    prompt=f"Email for {title}",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    print(response['choices'][0]['text']) 

    return response['choices'][0]['text']
    # return "OPENAI FUnction is working"


def SendEmail(sender_email, receiver_email, body, title):

    ## FILE TO SEND AND ITS PATH
    filename = 'some_file.csv'
    SourcePathName  = 'C:/reports/' + filename 

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = title
    body = body
    msg.attach(MIMEText(body, 'plain'))

    ## ATTACHMENT PART OF THE CODE IS HERE
    # attachment = open(r'C:\xampp\htdocs\website\Hackathons\testing codes\email.py', 'rb')
    # part = MIMEBase('application', "octet-stream")
    # part.set_payload((attachment).read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    # msg.attach(part)

    try:
        print("Message Sending......")
        server = smtplib.SMTP('smtp.office365.com', 587)  ### put your relevant SMTP here
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('jatintiwari123@outlook.com', 'Jatin!@#$1')  ### if applicable
        server.send_message(msg)
        server.quit()
        print("Message Sent")

    except:
        print("Error")
        server.quit()

<<<<<<< HEAD
=======




>>>>>>> 7d21bd9e4ebb7e195b35bae16345f8e33bc3697f
