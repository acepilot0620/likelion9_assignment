from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.wordCount, name="wc"),
    path('result/', views.result, name="result"),

]