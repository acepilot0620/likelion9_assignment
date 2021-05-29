from django.shortcuts import render

def welcome(request):
    return render(request, "welcome.html") # welcome.html 을 띄운다

def hello(request):
    userName = request.GET['name']
    return render(request, "hello.html", {'userName':userName})

