
from django.shortcuts import render
from .models import contato
import datetime
from .forms import ContatoForm
# Create your views here.
def index(request):
    return render(request, 'index.html')

def contato (request):
    data = {}
    forms = ContatoForm(request.POST or None)
        
    if str (request.method) == 'post':
        if forms.is_valid():
            descrição = forms.cleaned_data ['descrição']
            valor = forms.cleaned_data['valor']
            observações = forms.cleaned_data['observações']
            

            print("mensagem enviada!")
            print('descrição: ',descrição)
            print('valor: ', valor)
            print('observações: ',observações)
            
            messages.sucess(request, 'tudo ok!')
            forms = ContatoForm()
        else:
            messages.error(request, 'tem algo errado!')
    data['form']= forms
    return render(request, 'contato.html', data)

def produto(request):
    return render(request, 'produto.html')