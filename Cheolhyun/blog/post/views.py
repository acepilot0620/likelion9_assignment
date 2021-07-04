from django.shortcuts import render, redirect
from .models import Post

# Create your views here.

def new_post(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post()
        post.title = title
        post.content = content
        post.save()
        return redirect('main')
    return render(request, 'post.html')

def post_list(request):
    return render(request, 'post_list.html')