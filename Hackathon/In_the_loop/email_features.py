import os
import openai

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders



def openAI():

    openai.api_key ="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"

    search  = input("Email for : ")

    response = openai.Completion.create(
    model="text-davinci-002",
    prompt=f"Email for {search}",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    print(response['choices'][0]['text']) 


def SendEmail():

    ## FILE TO SEND AND ITS PATH
    filename = 'some_file.csv'
    SourcePathName  = 'C:/reports/' + filename 

    msg = MIMEMultipart()
    msg['From'] = 'jatintiwari123@outlook.com'
    msg['To'] = 'akshaymetry@gmail.com'
    msg['Subject'] = 'Report Update'
    body = 'Body of the message goes in here'
    msg.attach(MIMEText(body, 'plain'))

    ## ATTACHMENT PART OF THE CODE IS HERE
    attachment = open(r'C:\xampp\htdocs\website\Hackathons\testing codes\email.py', 'rb')
    part = MIMEBase('application', "octet-stream")
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)

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



