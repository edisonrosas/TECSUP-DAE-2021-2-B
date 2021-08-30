from django.urls import path 
from . import views

app_name= 'calculadora'

urlpatterns = [
    #ex : /calculadora/
    path('', views.index, name="index"),
    path('enviar', views.enviar, name="enviar"),
]
