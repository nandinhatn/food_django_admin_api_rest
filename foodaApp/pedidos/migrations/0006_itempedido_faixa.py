# Generated by Django 4.1.13 on 2024-02-28 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faixas', '0003_faixas_name'),
        ('pedidos', '0005_itempedido_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='itempedido',
            name='faixa',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='faixas.faixas'),
        ),
    ]
