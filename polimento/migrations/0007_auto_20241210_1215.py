# Generated by Django 3.2.4 on 2024-12-10 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polimento', '0006_chapas_polidas_polimento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='polimento',
            name='acabamento',
        ),
        migrations.RemoveField(
            model_name='polimento',
            name='bloco',
        ),
        migrations.RemoveField(
            model_name='polimento',
            name='chapas_quebradas',
        ),
        migrations.RemoveField(
            model_name='polimento',
            name='chapas_trincadas',
        ),
        migrations.RemoveField(
            model_name='polimento',
            name='finalizado',
        ),
        migrations.RemoveField(
            model_name='polimento',
            name='frequencia',
        ),
        migrations.RemoveField(
            model_name='polimento',
            name='qualidade',
        ),
        migrations.RemoveField(
            model_name='polimento',
            name='velocidade',
        ),
        migrations.AddField(
            model_name='chapas_polidas',
            name='frequencia',
            field=models.PositiveIntegerField(default=1),
        ),
    ]