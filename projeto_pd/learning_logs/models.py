from django.db import models

# Create your models here.
class Topico(models.Model):
    """ Um tópico que o usuário está aprendendo """
    text = models.CharField(max_length=200)
    data_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    
class Entrada(models.Model):
    """ Algo específico aprendido sobre um tópico """
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE)
    texto = models.TextField()
    data_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entradas'

    def __str__(self):
        """ Retorna uma string simples representando a entrada """
        return f'{self.texto[:50]}...'
