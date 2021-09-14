from django.contrib import admin
from django.urls import path
from Mainpage import views

urlpatterns = [
    path('', views.index, name='main'),
    path('result/', views.result, name='main2'),
]
