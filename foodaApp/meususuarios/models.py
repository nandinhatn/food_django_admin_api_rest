from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    age = models.IntegerField(blank=True, null=True)
    name= models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name= "teste"
        verbose_name_plural= "Usuário"


    