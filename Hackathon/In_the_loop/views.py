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
        print(MyDict)

        MyDict=dict(MyDict.lists()) 
        print(MyDict)
        title = MyDict["Title"]
        print(title[0])
        title = email_features.openAI(title[0]) #calling the funciton with title parameter
        email_body = { 
            'title' : title
        }
        return render(request, 'OpenAi.html', email_body) #If something enters then this 
    return render(request, 'OpenAi.html') #Or otherwise this will print

def chart(request):
    return render(request, 'chart.html')



