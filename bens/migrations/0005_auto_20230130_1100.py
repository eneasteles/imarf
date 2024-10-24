# Generated by Django 3.2.4 on 2023-01-30 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bens', '0004_veiculo_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='bem',
            name='ano',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bem',
            name='marca',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bem',
            name='modelo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bem',
            name='serial',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
