# Generated by Django 3.2.4 on 2023-01-12 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedreira', '0006_producao_pedreira_m3_m3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producao_pedreira_m3',
            name='m3',
            field=models.FloatField(),
        ),
    ]
