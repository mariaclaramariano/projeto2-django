
from django.shortcuts import render
from .models import contato
import datetime
from django.contrib import messages
from .forms import ContatoForm,produtoModelForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import produto
from django.shortcuts import redirect

# Create your views here.
def index(request):
    context = {
        'produtos': produto.objects.all()}

    return render(request, 'index.html', context)

def contato (request):
    
    forms = ContatoForm(request.POST or None)
    
    if forms.is_valid() :
        
            forms.send_mail()    
            messages.success(request, 'tudo ok!')
            forms = ContatoForm()
    else:
                messages.error(request, 'tem algo errado!')
        
    context = {'form' : forms}
    return render(request, 'contato.html', context)

def produto1 (request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == "POST":
                forms= produtoModelForm(request.POST, request.FILES)
                if forms.is_valid() :
                    forms.save()

                    messages.success(request, ' produto salvo com sucesso!')
                else:
                    messages.error(request, 'erro ao salvar o produto!')
        else:   
            forms = produtoModelForm()
        context = {
            'form': forms }
        return render(request, 'produto.html', context)
    else :
        return redirect(index)