from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def hello(request):
    userName = request.GET['name']
    userContent = request.GET['content']
    return render(request, 'hello.html', {'submittedName' : userName, 'submittedContent' : userContent})
