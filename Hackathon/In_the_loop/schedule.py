import os
from unittest import result
import schedule
import datetime
import time
import smtplib
import mysql.connector  

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders, message
def Send_Email(email,message):
    send_email_counter = 0
    ## FILE TO SEND AND ITS PATH
    filename = 'some_file.csv'
    SourcePathName  = 'C:/reports/' + filename 

    msg = MIMEMultipart()
    msg['From'] = 'akshaymetry123@outlook.com'
    msg['To'] = email
    msg['Subject'] = 'Report Update'
    body = message
    msg.attach(MIMEText(body, 'plain'))

    ## ATTACHMENT PART OF THE CODE IS HERE
    attachment = open(r'C:/Users/aksha/Desktop/Hackathon/test.txt', 'rb')
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
        server.login('akshaymetry123@outlook.com', 'akshay@123')  ### if applicable
        server.send_message(msg)
        server.quit()
        print("Message Sent")
        send_email_counter = send_email_counter+1
    except:
        print("Error")
        # server.quit()

# def fetch_data():
    

#     return email_id,message,date


def email_schedule():
    myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "",database = "email_database")  
    #printing the connection object   
    mycursor = myconn.cursor()
    mycursor.execute("select * from email_data")
    today = datetime.datetime.today()
    date_today = today.strftime("%Y-%m-%d")
    # print(type(date_today))
    # list of data items
    result = mycursor.fetchall()
    for i in result:
        email_id = i[1]
        message = i[2]
        date = str(i[3])
        if date == date_today:
            # schedule.every().day.at("09:06").do(SendEmail(email_id,message))
            Send_Email(email_id,message)
        else:
            print("Email not Sent")
    # schedule.every().day.at("09.06").do(SendEmail)
    # schedule.every(2).seconds.do(SendEmail)
    
email_schedule()
schedule.every().day.at("12:55").do(Send_Email)
# schedule.every(1).seconds.do(email_schedule) 
# schedule.every().hour.do(mail)
# schedule.every().day.at("10:30").do(email_schedule)
# schedule.every().day.at("01:00").do(email_schedule)
# schedule.every(5).to(10).minutes.do(mail)
# schedule.every().monday.do(mail)
# schedule.every().wednesday.at("13:15").do(mail)
# schedule.every().minute.at(":17").do(mail)
# SendEmail()

# while True:
#     schedule.run_pending()
#     time.sleep(1)

# def save_draft():
