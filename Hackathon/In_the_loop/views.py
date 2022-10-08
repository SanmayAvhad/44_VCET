from email import message
from pickle import TRUE
import mysql.connector  
from django.shortcuts import render
from In_the_loop import email_features

def index(request):

    print(request.GET)
    print("MY namme is jatin")

    context = {
        "first_name": "Jatin",
        "last_name": "Tiwari",
        "address": "Mumbai, India"
    }
           
    return render(request, 'index.html', context)

def index(request):
    return render(request, 'index.html')


def Schedule(request): 
    if request.method == 'POST':
        print("jatin")
        SaveDict=request.POST

        SaveDict=dict(SaveDict.lists()) 
        # print("data:",SaveDict)
        # data: {''to': [''], 'from': [''], 'title': [''], 'message': [''], 'date': [''], 'time': ['']}
        to = SaveDict["to"]
        sender = 'akshaymetry123@outlook.com'
        title = SaveDict["title"]
        message = SaveDict["message"]
        date = SaveDict["date"]
        to = to[0]
        
        message = message[0]
        title = title[0]
        date = date[0]
        print(type(message))
        # sender = SaveDict["from"][0]
        # message = SaveDict["message"][0] 
        print(to,sender,title,message,date)
        
        myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "",database = "email_database")  
        #printing the connection object   
        mycursor = myconn.cursor()
        
    
        mysql_insert_query = "insert into email_data(sender,email_id,title,message,date) values(%s,%s,%s,%s,%s)"
        record = [sender,to,title,message,date]
        
        # mycursor.execute("insert into email_data(sender,email_id,title,message,date) values({sender},'{to}','{title}','{message}','{date}')")
        mycursor.execute(mysql_insert_query,record)
        myconn.commit()
 
    return render(request, 'Schedule.html') 


def OpenAi(request):
    

    if request.method == 'POST':
        MyDict=request.POST
        # print(MyDict)

        MyDict=dict(MyDict.lists()) 
        print(MyDict)
        title = MyDict["Title"]
        # print(title)
        title =title[0]
        sender_email = MyDict["user_email"][0] 
        receiver_email = MyDict["receiver_email"][0]
        # auto = MyDict["auto"]

        # print(auto)
        

       
        # auto=MyDict["auto"][0]
        # print(auto)
            
        body = email_features.openAI(title) #calling the funciton with title parameter
                

        
        message_sent = email_features.SendEmail(sender_email, receiver_email, body,title)
        print("Email SEnt")
            
            
        


        email_body = { 'title' : title, 'body' : body,  'user_email': sender_email, 'receiver_email' : receiver_email, }


        return render(request, 'OpenAi.html', email_body) #If something enters then this 


    return render(request, 'OpenAi.html') #Or otherwise this will print

def chart(request):
    return render(request, 'chart.html')



