# Generated by Django 3.2.4 on 2022-05-10 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outlet', '0002_produto_de_venda_exportacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto_de_venda',
            name='observacao',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
