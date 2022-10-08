from email import message
from pickle import TRUE
import mysql.connector 
from django.shortcuts import render
from In_the_loop import email_features

def index(request):
    if request.method == 'POST':
        MyDict=request.POST
        MyDict=dict(MyDict.lists()) 
        print(MyDict)
        print("mihihr") 
        sync = MyDict["sync"][0]

        if sync=='sync':
            email_list= email_features.receive_emails()
            print(email_list)
            print(type(email_list))
            print("mihihr")


            email_data = {

                'sender1': email_list[0][0],
                'subject1': email_list[0][1],
                'body1':email_list[0][2],

                'sender2': email_list[1][0],
                'subject2': email_list[1][1],
                'body2':email_list[1][2], 
 

                'sender3': email_list[2][0],
                'subject3': email_list[2][1],
                'body3':email_list[2][2],

                'sender5': email_list[3][0],
                'subject5': email_list[3][1],
                'body5':email_list[3][2],

                'sender5': email_list[4][0],
                'subject5': email_list[4][1],
                'body5':email_list[4][2],

            }
        
            print(email_data)
        # print(case_list[0]['key2'])
       
            return render(request, 'index.html', email_data)
    return render(request, 'index.html') 

def signin(request):
    return render(request,'signin.html')

def signup(request):
    return render(request,'signup.html')

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



