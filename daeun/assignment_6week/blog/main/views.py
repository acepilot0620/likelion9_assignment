from django.shortcuts import render
from collections import Counter

# Create your views here.
def main(request):
    return render(request, 'main.html')

def word_count(request):
    if request.method == 'POST':
        text=request.POST.get('text_input')
        
        if text:
            result={}
            word=text.lower().split()
            word=Counter(word)
            for item in word:
                word_count=str(word[item]) #숫자부분(vlaue) 입력
                result[item]=str(word_count) #key 부분 입력
        return render(request, 'word_count.html', {'result':result, 'text':text})

    return render(request, 'word_count.html')