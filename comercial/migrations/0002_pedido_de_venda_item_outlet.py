# Generated by Django 3.2.4 on 2021-11-19 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comercial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido_de_venda_item',
            name='outlet',
            field=models.IntegerField(blank=True, default=0, editable=False, null=True),
        ),
    ]