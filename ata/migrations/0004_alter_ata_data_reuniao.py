# Generated by Django 3.2.4 on 2023-06-20 15:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ata', '0003_alter_ata_data_reuniao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ata',
            name='data_reuniao',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]