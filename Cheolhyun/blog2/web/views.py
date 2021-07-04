from typing_extensions import ParamSpecKwargs
from django.shortcuts import render,get_object_or_404
from .models import Web
# Create your views here.

def home(request):
    webs = Web.objects.all()
    return render(request, 'home.html', {'webs':webs})

def detail(request, id):
    web = get_object_or_404(Web, pk = id)
    return render(request,'detail.html',{'web':web})