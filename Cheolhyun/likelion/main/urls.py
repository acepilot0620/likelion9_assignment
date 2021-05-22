from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main,name="main"),
    path('detail/',views.detail,name='detail'),
    path('abc/', views.abc, name='abc'),
]