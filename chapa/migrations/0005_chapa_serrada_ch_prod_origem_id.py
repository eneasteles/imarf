# Generated by Django 3.2.4 on 2023-01-19 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapa', '0004_auto_20230119_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapa',
            name='serrada_ch_prod_origem_id',
            field=models.BigIntegerField(default=1),
        ),
    ]