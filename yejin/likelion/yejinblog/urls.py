from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"), # main.html
    path('guest/', views.guest, name="guest"), #guest.html
    # path('word_count/', views.word_count, name="word_count"),
    path('login/', views.login, name="login")
]