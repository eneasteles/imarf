# Generated by Django 3.2.4 on 2023-02-02 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0022_alter_resinamento_chapa_bloco'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resinamento_chapa',
            name='bloco',
        ),
    ]
