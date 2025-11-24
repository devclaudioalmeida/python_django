from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topico, Entrada
from .forms import FormularioTopico, EntradaFormulario

def checa_proprietario_topico(request):
    if topico.owner != request.user:
        raise Http404

# Create your views here.
def index(request):
    """ A pagina inicial para o registro de aprendizagem """
    return render(request, 'learning_logs/index.html')


@login_required
def topicos(request):
    """ Mostra todos os tópicos """
    tp = Topico.objects.filter(owner=request.user).order_by('data_add')
    contexto = {'topicos' : tp}
    return render(request, 'learning_logs/topicos.html', contexto)


@login_required
def topico(request, id_topico):
    """ Mostra um único tópico e todas as sua entradas"""
    topico = Topico.objects.get(id=id_topico)
    # Verifica se o tópico pertence ao usuário atual
    checa_proprietario_topico(request)
    entradas = topico.entrada_set.order_by('-data_add')
    contexto = {'topico' : topico, 'entradas' : entradas}
    return render(request, 'learning_logs/topico.html', contexto)


@login_required
def novo_topico(request):
    """ Adiiona um novo tópico """
    if request.method != 'POST':
        # Nenhum dado enviado; cria um formulário em branco
        form = FormularioTopico()
    else:
        # Dados POST enviados: processa os dados
        form = FormularioTopico(data=request.POST)
        if form.is_valid():
            novo_topico = form.save(commit=False)
            novo_topico.owner = request.user
            novo_topico.save()
            return redirect('learning_logs:topicos')
        
    # Exibe um formulário em branco ou inválido
    context = {'form' : form}
    return render(request, 'learning_logs/novo_topico.html', context)


@login_required
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
            return redirect('learning_logs:topico', id_topico=id_topico)
    
    # Exibe um formulário em branco ou inválido
    context = {'topico' : topico, 'form' : form}
    return render(request, 'learning_logs/nova_entrada.html', context)


@login_required
def editar_entrada(request, id_entrada):
    """ Edita uma entrada existente """
    entrada = Entrada.objects.get(id=id_entrada)
    topico = entrada.topico
    checa_proprietario_topico(request)

    if request.method != 'POST':
        # Requisição inicial; pre-preenche o formulário com a entrada atual.
        form = EntradaFormulario(instance=entrada)
    else:
        # Dados POST enviados; processa os dados
        form = EntradaFormulario(instance=entrada, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topico', id_topico=topico.id)
    
    context = {'entrada' : entrada, 'topico' : topico, 'form' : form}
    return render(request, 'learning_logs/editar_entrada.html', context)