# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Metrics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='rawdataint',
            name='name',
        ),
        migrations.AddField(
            model_name='rawdata',
            name='rawDataInt',
            field=models.ForeignKey(to='Metrics.RawDataInt'),
        ),
        migrations.AddField(
            model_name='metriclog',
            name='value',
            field=models.ForeignKey(default=None, to='Metrics.RawData'),
            preserve_default=False,
        ),
    ]
