# Generated by Django 3.2.4 on 2022-08-02 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polimento', '0009_remove_jogo_de_abrasivos_pausado'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogo_de_abrasivos',
            name='finalizado',
            field=models.BooleanField(default=False),
        ),
    ]
