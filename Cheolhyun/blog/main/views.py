from django.shortcuts import render, redirect

wordused = { }

def set_key(dictionary, key):
    if key not in dictionary:
        dictionary[key] = int(1)
    else:
        dictionary[key] = [int(dictionary[key]+1)]

def home(request):
    if request.method == "POST":
        text = request.POST.get('textInput')
        blank_list = text.split(' ')
        blank_num = len(blank_list)

        word_num = len(text)

        word_notblank_num = len(text) - text.count(' ')

        return render(request, 'home.html', {"blank_num":blank_num, "text":text, "word_num":word_num, "word_notblank_num":word_notblank_num})

    if request.method == "POST":
        text2 = request.POST.get('wordusedInput')
        blank_divide = text2.split(' ')
        for i in range(len(blank_divide)):
            set_key(wordused, blank_divide[i])

        return render(request, 'home.html', {"keys":list(wordused.keys()), "text2":text2, "values":list(wordused.values())})
        
    return render(request, "home.html")

def hello(request):
    userName = request.GET['name']
    userContent = request.GET['content']
    return render(request, 'hello.html', {'submittedName' : userName, 'submittedContent' : userContent})

def login(request):
    if request.method == "POST": # 사용자가 로그인 버튼을 눌렀을 때
        username_DB = 'testid'
        password_DB = '1234'
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username_DB == username and password_DB == password:
            return redirect('home')
        elif username_DB == username and password != password_DB:
            error_msg = "비밀번호 오류"
            return render(request, 'login.html', {"error_msg":error_msg})
        else:
            error_msg = "아이디 오류"
            return render(request, 'login.html', {"error_msg":error_msg})
    return render(request, 'login.html')
