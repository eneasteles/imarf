# Generated by Django 3.2.4 on 2021-06-30 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0006_auto_20210628_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapas_produzidas',
            name='altura',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='chapas_produzidas',
            name='comprimento',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='chapas_produzidas',
            name='largura',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
    ]