from enum import auto
from pickle import TRUE
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
    return render(request, 'Schedule.html')



def OpenAi(request):

    if request.method == 'POST':
        MyDict=request.POST
        # print(MyDict)

        MyDict=dict(MyDict.lists()) 
        # print(MyDict)
        title = MyDict["Title"]
        # print(title)
        title =title[0]
        sender_email = MyDict["user_email"][0] 
        receiver_email = MyDict["receiver_email"][0]
        

        # print(receiver_email)

        try:
            auto=MyDict["auto"][0]
            print(auto)
            if auto == '0':
                body = email_features.openAI(title) #calling the funciton with title parameter
                

        except: 
            
            email_features.SendEmail(sender_email, receiver_email, body)

        


        email_body = { 'title' : title, 'body' : body,  'user_email': sender_email, 'receiver_email' : receiver_email, }


        return render(request, 'OpenAi.html', email_body) #If something enters then this 


    return render(request, 'OpenAi.html') #Or otherwise this will print

def chart(request):
    return render(request, 'chart.html')



