from django.contrib import admin
from .models import produto
# Register your models here.

@admin.register(produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ( 'nome', 'preco','estoque', 'slug', 'criado', 'modificado', 'ativo' )