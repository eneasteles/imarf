# Generated by Django 3.2.4 on 2021-11-23 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comercial', '0007_alter_forma_de_pagamento_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='forma_de_pagamento',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
    ]
