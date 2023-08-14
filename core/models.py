from django.db import models
from stdimage import StdImageField
#signals
from django.db.models import signals
from django.template.defaultfilters import slugify

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
    email = models.EmailField(max_length=100, default=True )
class meta:
    verbose_name_plural =  'contato'

class base (models.Model):
    criado = models.DateField('data de criação', auto_now_add=True)
    modificado= models.DateField('data de atualização', auto_now=True)
    ativo= models.BooleanField('ativo?', default=True)

    class meta:
        abstract = True
class produto(base):
    nome = models.CharField('nome:', max_length=100)
    preco = models.DecimalField('preço', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('estoque')
    imagem = StdImageField('imagem', upload_to='produtos', variations= {'thumb': (124,123)})
    slug = models.SlugField('slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome
def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug= slugify(instance.nome)

signals.pre_save.connect(produto_pre_save, sender=produto)