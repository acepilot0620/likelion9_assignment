from django.shortcuts import render

def main(request):
    return render(request,"main.html")

def guest(request):
    userName = request.GET['name']
    # guest.html에서 이름 가져오기
    return render(request,"guest.html", {'userName':userName})
    # hello.html로 userName이라는 이름을 가진 값이 들어가게 된다.


