# Generated by Django 3.2.4 on 2021-07-22 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0025_material_pedreira'),
    ]

    operations = [
        migrations.AddField(
            model_name='resinamento_item',
            name='quantidade_insumo',
            field=models.FloatField(default=0),
        ),
    ]