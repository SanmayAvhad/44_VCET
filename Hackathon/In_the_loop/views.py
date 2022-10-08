from pickle import TRUE
from re import I
from django.shortcuts import render
from In_the_loop import email_features

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



