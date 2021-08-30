from django.shortcuts import render
from math import pi
# Create your views here.
def index(request):
    return render(request, 'cilindro/formulario.html')

def enviar(request):
    diametro = float(request.POST['diametro'])
    altura = float(request.POST['altura'])
    volumen = (pi*((diametro/2)**2)) * altura

    context = {      
        'volumen' : volumen, 
    }
    return render(request, 'cilindro/resultado.html', context)