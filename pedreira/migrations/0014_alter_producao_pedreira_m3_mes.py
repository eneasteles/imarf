# Generated by Django 3.2.4 on 2023-04-04 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedreira', '0013_auto_20230308_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producao_pedreira_m3',
            name='mes',
            field=models.IntegerField(default=4),
        ),
    ]