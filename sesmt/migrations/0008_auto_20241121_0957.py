# Generated by Django 3.2.4 on 2024-11-21 12:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sesmt', '0007_alter_pdfdocument_uploaded_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdfdocument',
            name='emissao_documento',
            field=models.DateField(default=datetime.datetime.now, help_text='Data de emissão do documento que se refere ao mês e ano do documento.'),
        ),
        migrations.AlterField(
            model_name='pdfdocument',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
