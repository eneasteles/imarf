# Generated by Django 3.2.4 on 2021-07-07 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0010_auto_20210707_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='view_serrada',
            name='material',
            field=models.CharField(default='', max_length=100),
        ),
    ]