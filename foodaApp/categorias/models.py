from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    class Meta():
        verbose_name_plural  = 'Categoria'
        verbose_name= 'Categoria'
  

    def __str__(self):
        return self.name