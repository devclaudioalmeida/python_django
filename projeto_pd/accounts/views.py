from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """ Cadastra um usuário novo """
    if request.method != 'POST':
        # Exibe o formulário em brando de cadastro
        form = UserCreationForm()
    else:
        # Processa o formulário preenchido
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Faz o login do usuário e o redirecona para a página inicial
            login(request, new_user)
            return redirect('learning_logs:index')
        
    # Exibe um formulário em brando ou inválido
    context = {'form' : form}
    return render(request, 'registration/register.html', context)
