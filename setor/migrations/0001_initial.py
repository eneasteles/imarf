# Generated by Django 3.2.4 on 2023-02-15 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('setor', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
    ]
