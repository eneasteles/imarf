# Generated by Django 3.2.4 on 2024-12-10 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polimento', '0005_auto_20241210_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapas_polidas',
            name='polimento',
            field=models.ForeignKey(default=108, on_delete=django.db.models.deletion.CASCADE, to='polimento.polimento'),
            preserve_default=False,
        ),
    ]
