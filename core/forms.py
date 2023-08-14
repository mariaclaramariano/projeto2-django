from django.db import models
from django.forms import ModelForm
from .models import contato
from django.core.mail.message import EmailMessage
from .models import produto
from django import forms

class ContatoForm(ModelForm):

    class Meta:
       model = contato
       fields = ['descrição', 'email', 'observações']

    def send_mail(self):
        descrição = self.cleaned_data['descrição']
        email = self.cleaned_data['email']
        observações = self.cleaned_data['observações']
        
        conteudo = f'descrição: {descrição}\n e=mail: {email}\n observações: {observações}'
       
        email = EmailMessage(
            subject = 'e-mail enviado pelo sistema django2',
            body = conteudo,
            from_email='contato@seudominio.com.br',
            to= ['contato@seudominio.com.br',],
            headers= {'reply-to' : email}

        )

        email.send()



class produtoModelForm(forms.ModelForm):
  class Meta:
    model = produto
    fields = ['nome', 'preco', 'estoque', 'imagem']