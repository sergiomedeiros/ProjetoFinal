# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jogos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('clube_casa', models.CharField(max_length=30)),
                ('clube_visitante', models.CharField(max_length=30)),
                ('gol_clube_casa', models.IntegerField()),
                ('gol_clube_visitante', models.IntegerField()),
                ('adiado', models.BooleanField()),
                ('data_cadastro', models.DateField()),
            ],
        ),
    ]
