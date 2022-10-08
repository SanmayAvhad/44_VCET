from pickle import TRUE
from pyexpat.errors import messages
from re import I
from django.http import HttpResponse
from django.shortcuts import render,redirect
from requests import post
from In_the_loop import email_features
from django.contrib.auth.models import User

def index(request):
    print("MY namme is jatin")
    if request.method == 'POST':
        print(request.POST)
        MyDict=dict(MyDict.lists()) 
        print(MyDict)
        sync = MyDict["sync"][0]

        if sync=='sync':
            all_email= email_features.receive_emails()
            print(all_email)

        
        # print(case_list[0])
        # print(case_list[0]['key2'])
       
    return render(request, 'index.html', context)

def signin(request):
    return render(request,'signin.html')

def signup(request):
    return render(request,'signup.html')

def index(request):
    return render(request, 'index.html')


def Schedule(request): 
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


def HandleSignup(request):
    if request.method == 'POST':
        Username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        fname = request.POST['fname']
        lname = request.POST['lname']

        # Create user
        myUser = User.objects.create_user(Username,email,password)
        myUser.fname = fname
        myUser.lname = lname
        myUser.save()
        return redirect('/')

    else:
        return HttpResponse("404 Not Found")
    
