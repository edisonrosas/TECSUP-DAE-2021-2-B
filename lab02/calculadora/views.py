from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'titulo': "Formulario",
    }

    return render(request, 'calculadora/formulario.html', context)

def enviar(request):
    operacion = request.POST['operacion']
    val1 = int(request.POST['value01'])
    val2 = int(request.POST['value02'])
    operador = ""
    resultado = 0
    #Identificamos el operador y resultado correspondiente según la operación a realizar 
    
    if operacion == 'suma':
        operador='+'
        resultado=val1+val2
    elif operacion == 'resta':
        operador='-'
        resultado=val1-val2
    elif operacion == 'multiplicación':
        operador='x'
        resultado=val1*val2

    context = {      
        'titulo' : "Resultado",
        'operacion' :  operacion,
        'value01' : val1,
        'value02' : val2,
        'operador' : operador,
        'resultado' : resultado, 
    }
    return render(request, 'calculadora/resultado.html', context)