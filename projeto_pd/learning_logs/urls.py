""" Define padrões de url para learning logs """

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Página Inicial
    path('', views.index, name='index'),
    # Pagina que mostra todos os tópicos
    path('topicos/', views.topicos, name='topicos'),
]