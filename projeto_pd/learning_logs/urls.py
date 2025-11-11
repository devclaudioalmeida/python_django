""" Define padrões de url para learning logs """

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Página Inicial
    path('', views.index, name='index'),
    # Pagina que mostra todos os tópicos
    path('topicos/', views.topicos, name='topicos'),
    path('topicos/<int:id_topico>/', views.topico, name='topico'),
    # Página para adicionar um tópico novo
    path('novo_topico/', views.novo_topico, name='novo_topico'),
    # Página para adicionar uma entrada nova
    path('nova_entrada/<int:id_topico>/', views.nova_entrada, name='nova_entrada'),
]