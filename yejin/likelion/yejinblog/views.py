from django.shortcuts import render, redirect

def main(request):
    if request.method == "POST": 
        text = request.POST.get('text_input') # post method를 사용해서 text_input을 가져오자(Get)
        word_list = text.split(' ')
        word_num = len(word_list)
        return render(request,"main.html", {"word_num":word_num}, {"text":text})
    return render(request,"main.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        username_DB = "yexjin"
        password_DB = "1234"
        if username == username_DB and password == password_DB:
            return redirect('main')
        else:
            error_message= "틀렸어요"
            return render(request, 'login.html', {"error_message" : error_message})
    return render(request, "login.html")

def guest(request):
    userName = request.GET['name']
    # guest.html에서 이름 가져오기
    return render(request,"guest.html", {'userName':userName})
    # hello.html로 userName이라는 이름을 가진 값이 들어가게 된다.

# def word_count(request):
#     text = request.POST.get('text_input') # post method를 사용해서 text_input을 가져오자(Get)
#     word_list = text.split(' ')
#     print(word_list)

#     return render(request, "main.html", {})

