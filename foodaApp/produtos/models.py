from django.db import models

from categorias.models import Category

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    meiaPorcao = models.BooleanField(default=True)
    imagem= models.ImageField(upload_to='static/imagens/', default='default.jpg')
    
    categoria =models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    class Meta():
        verbose_name_plural  = 'Produto'

    def __str__(self):
        return self.name