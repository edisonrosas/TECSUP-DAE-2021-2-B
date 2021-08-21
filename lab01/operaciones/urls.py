from django.urls import path
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    # ex: localhost:8080/polls/
    path('', views.index, name='index'),

    path('sumar/<int:num1>/<int:num2>/', views.suma, name='suma'),
 
    path('restar/<int:num1>/<int:num2>/', views.resta, name='resta'),
   
    path('multiplicar/<int:num1>/<int:num2>/', views.multiplicacion, name='multiplicacion'),
]
