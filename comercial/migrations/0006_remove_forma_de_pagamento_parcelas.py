# Generated by Django 3.2.4 on 2021-11-22 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comercial', '0005_auto_20211122_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forma_de_pagamento',
            name='parcelas',
        ),
    ]