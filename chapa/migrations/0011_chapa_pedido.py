# Generated by Django 3.2.4 on 2023-01-24 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapa', '0010_auto_20230124_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapa',
            name='pedido',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
