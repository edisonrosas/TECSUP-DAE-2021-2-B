from django.shortcuts import get_object_or_404,render 
from django.http import HttpResponse,HttpResponseRedirect 
from django.urls import reverse

from .models import Option,Pregunta
# Create your views here.

def index(request):
    latest_question_list= Pregunta.objects.order_by('pub_date')[:5]
    context = {'latest_question_list' : latest_question_list}
    return render(request, './index.html', context)

def detalle(request, pregunta_id):
    pregunta=get_object_or_404(Pregunta, pk=pregunta_id)
    return render(request,'./detalle.html',{'pregunta':pregunta})

def votar(request, pregunta_id):
    pregunta=get_object_or_404(Pregunta, pk=pregunta_id)
    try:
        selected_opcion=pregunta.option_set.get(pk=request.POST['opcion'])
    except (KeyError, Option.DoesNotExist):
        return render(request, './detalle.html', {
            'pregunta':pregunta,
            'error_message': "No has seleccionado una opcion.",
        })
    else:
        selected_opcion.votos +=1
        selected_opcion.save()
        return HttpResponseRedirect(reverse('encuesta:detalle', args=(pregunta.id,)))

def resultados(request, pregunta_id):
    pregunta=get_object_or_404(Pregunta, pk=pregunta_id)
    return render(request,'./resultados.html', {'pregunta': pregunta} )