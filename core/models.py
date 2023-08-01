from django.db import models

# Create your models here.
class categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateField(auto_now_add=True)

class contato(models.Model):
    data = models.DateTimeField(auto_now=True)
    descrição = models.CharField(max_length=10)
    valor= models.DecimalField(max_digits=7, decimal_places=2)
    categoria= models.ForeignKey( categoria,on_delete=models.CASCADE)
    observações = models.TextField(null=True, blank=True)

class meta:
    verbose_name_plural =  'contato'