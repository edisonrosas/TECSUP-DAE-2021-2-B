from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Respuesta de la vista de Encuestas")
    
def suma(request, num1, num2):
    return HttpResponse("La suma de %i + %i = %i" % (num1,num2,num1+num2))

def resta(request, num1, num2):
    return HttpResponse("La resta de %i - %i = %i" % (num1,num2,num1-num2))

def multiplicacion(request, num1, num2):
    return HttpResponse("La multiplicación de %i x %i = %i" % (num1,num2,num1*num2))
