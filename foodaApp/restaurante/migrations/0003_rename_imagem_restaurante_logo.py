# Generated by Django 4.1.13 on 2024-02-23 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0002_restaurante_imagem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurante',
            old_name='imagem',
            new_name='logo',
        ),
    ]
