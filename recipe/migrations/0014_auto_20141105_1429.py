# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0013_hopsil_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='yeast_pitch_rate',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='subtype',
            field=models.CharField(default='wheat ale', max_length=50, choices=[('Ale', (('wheat ale', 'Wheat Ale'), ('stout', ()))), ('Lager', (('generic lager', 'Bock'),))]),
            preserve_default=True,
        ),
    ]
