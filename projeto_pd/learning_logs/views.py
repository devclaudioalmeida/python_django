from django.shortcuts import render, redirect

from learning_logs.models import Topico
from .forms import FormularioTopico, EntradaFormulario

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


def novo_topico(request):
    """ Adiiona um novo tópico """
    if request.method != 'POST':
        # Nenhum dado enviado; cria um formulário em branco
        form = FormularioTopico()
    else:
        # Dados POST enviados: processa os dados
        form = FormularioTopico(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topicos')
    # Exibe um formulário em branco ou inválido
    context = {'form' : form}
    return render(request, 'learning_logs/novo_topico.html', context)


def nova_entrada(request, id_topico):
    """ Adicinona uma entrada nova para um tópico específico """
    topico = Topico.objects.get(id=id_topico)

    if request.method != 'POST':
        # Nenhum dado enviado; cria um formulário em branco
        form = EntradaFormulario()
    else:
        # Dados POST enviados; processa os dados
        form = EntradaFormulario(data=request.POST)
        if form.is_valid():
            nova_entrada = form.save(commit=False)
            nova_entrada.topico = topico
            nova_entrada.save()
            return redirect('learning_logs:topico', topic_id=id_topico)
    
    # Exibe um formulário em branco ou inválido
    context = {'topico' : topico, 'form' : form}
    return render(request, 'learning_log/nova_entrada.html', context)