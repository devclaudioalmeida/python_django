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
