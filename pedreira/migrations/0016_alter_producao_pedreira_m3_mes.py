# Generated by Django 3.2.4 on 2023-06-20 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedreira', '0015_alter_producao_pedreira_m3_mes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producao_pedreira_m3',
            name='mes',
            field=models.IntegerField(default=6),
        ),
    ]
