# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jogos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rodadas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('data', models.DateField()),
                ('data_cadastro', models.DateField()),
                ('jogos', models.ManyToManyField(to='jogos.Jogos')),
            ],
        ),
    ]
