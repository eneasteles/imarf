# Generated by Django 3.2.4 on 2022-08-24 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0008_auto_20220824_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloco',
            name='altura_bruto',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='bloco',
            name='comprimento_bruto',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='bloco',
            name='largura_bruto',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
    ]