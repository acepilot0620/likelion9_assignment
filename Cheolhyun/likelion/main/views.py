from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request,'main.html') #request가 들어왔을 때 main.html을 띄워준다

def detail(request):
    return render(request, 'detail.html')

def abc(request):
    userName = request.GET['name']
    return render(request, 'abc.html', {'userName' : userName})