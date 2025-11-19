""" Define padões de url para contas """

from django.urls import path, include

from . import views

app_name = 'accounts'
urlpatterns = [
    # Inclui Urls de autenticação default
    path('', include('django.contrib.auth.urls')),
    # Pagina de cadastros
    path('register', views.register, name='register'),
]