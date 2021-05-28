from django.shortcuts import redirect, render

def main(request):
    if request.method=="POST":
        text=request.POST.get('user_input')
        word_list=text.split(' ')
        word_num=len(word_list)
        return render(request,'home.html',{"word_num":word_num,"text":text})
    return render(request,'home.html')

def login(request):
    if request.method=="POST":
        username_DB="redpen0824"
        pwd_DB="0824"
        username =request.POST.get('username')
        pwd =request.POST.get('pwd')
        print(username,pwd)
        if username_DB == username and pwd_DB == pwd:
           return redirect('main')
        elif pwd !=pwd_DB:
            error_msg ="비밀번호 오류"
            return render(request, 'login.html',{"error_msg":error_msg})
        elif username !=username_DB:
            error_msg ="아이디 오류"
            return render(request, 'login.html',{"error_msg":error_msg})
    return render(request,'login.html')

def wordcount.html (request):
    render(request,'wordcount.html')

def wordcount.html(request):
    sentence = request.GET['sentence']

wordlist=sentence.split()

worddict={}

for word in wordlist:
   if word in worddict:
     worddict[word]+=1
   else :
     worddict[word]=1

return render(request, “result.html”,{‘fulltext’:sentence, ‘count’:len(wordlist),”worddict”:worddict.itms})

