# Generated by Django 3.2.4 on 2021-07-15 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0022_pedreira_centro_de_custo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resinamento',
            name='ano',
            field=models.IntegerField(default=2021),
        ),
        migrations.AlterField(
            model_name='resinamento_item',
            name='observacao',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]