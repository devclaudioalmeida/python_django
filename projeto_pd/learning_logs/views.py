from django.shortcuts import render

from learning_logs.models import Topico

# Create your views here.
def index(request):
    """ A pagina inicial para o registro de aprendizagem """
    return render(request, 'learning_logs/index.html')


def topicos(request):
    """ Mostra todos os tópicos """
    tp = Topico.objects.order_by('data_add')
    contexto = {'topicos' : tp}
    return render(request, 'learning_logs/topicos.html', contexto)


def topico(request, id_topico):
    """ Mostra um único tópico e todas as sua entradas"""
    topico = Topico.objects.get(id=id_topico)
    entradas = topico.entrada_set.order_by('-data_add')
    contexto = {'topico' : topico, 'entradas' : entradas}
    return render(request, 'learning_logs/topico.html', contexto)

