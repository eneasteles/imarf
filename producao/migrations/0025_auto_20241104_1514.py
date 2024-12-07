# Generated by Django 3.2.4 on 2024-11-04 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0024_auto_20230308_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blocoserrada',
            name='serrada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producao.serrada'),
        ),
        migrations.AlterField(
            model_name='chapas_produzidas',
            name='serrada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producao.serrada'),
        ),
        migrations.AlterField(
            model_name='custos_pedreira',
            name='ano',
            field=models.IntegerField(default=2024),
        ),
        migrations.AlterField(
            model_name='folha_de_pagamento',
            name='ano',
            field=models.IntegerField(default=2024),
        ),
        migrations.AlterField(
            model_name='parada',
            name='serrada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producao.serrada'),
        ),
    ]
