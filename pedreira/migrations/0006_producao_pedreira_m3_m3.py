# Generated by Django 3.2.4 on 2023-01-12 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedreira', '0005_remove_producao_pedreira_m3_m3'),
    ]

    operations = [
        migrations.AddField(
            model_name='producao_pedreira_m3',
            name='m3',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]