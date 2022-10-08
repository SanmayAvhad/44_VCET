import os
import openai

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders


def receive_emails():
    pass


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


