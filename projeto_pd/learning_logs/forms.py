from django import forms

from .models import Topico, Entrada

class FormularioTopico(forms.ModelForm):
    class Meta:
        model = Topico
        fields = ['text']
        labels = {'text': ''}

class EntradaFormulario(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['text']
        labels = {'text' : ''}
        widgets = {'text' : forms.Textarea(attrs={'cols' : 80})}