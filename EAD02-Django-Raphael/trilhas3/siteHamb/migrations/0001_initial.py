# Generated by Django 5.0.4 on 2024-05-04 18:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCliente', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11)),
                ('fone', models.CharField(max_length=15)),
                ('endereco', models.TextField()),
                ('date_create', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
