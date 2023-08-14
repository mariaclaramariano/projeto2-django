
from django.forms import ModelForm
from .models import contato


class ContatoForm(ModelForm):
    class Meta:
       model = contato
       fields = ['descrição','valor','observações']
