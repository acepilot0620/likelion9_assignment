from django.shortcuts import render, redirect

# Create your views here.
def main(request):
    if request.method == "POST":
        text = request.POST.get('user_input')
        word_list = text.split(" ")
        word_num = 0
        for i in word_list:
            if i=="":
                pass
            else:
                word_num+=1
        # word_num = len(word_list)
        return render(request, 'home.html', {'text':text, 'word_num' : word_num})
    return render(request, "home.html", )


from .models import login 
def login(request):
    if request.method == "POST":
        # user = login.objects.get(id = id)

        username_DB = "dldydgns53"
        password_DB = "1234"
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username_DB == username and password_DB == password:
            redirect('main')
        elif username_DB == username:
            error_msg = "비밀번호 오류"
            return render(request, 'login.html', {"error_msg":error_msg})
        else:
            error_msg = "둘다 틀렸어 바보야"
            return render(request, 'login.html', {"error_msg":error_msg})


    
    return render(request, "login.html", )