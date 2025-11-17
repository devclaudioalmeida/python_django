""" Define padões de url para contas """

from django.urls import path, include

app_name = 'accounts'
urlpatterns = [
    # Inclui Urls de autenticação default
    path('', include('django.contrib.auth.urls')),
]