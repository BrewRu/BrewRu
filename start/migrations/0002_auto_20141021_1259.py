# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='subtype',
            field=models.CharField(max_length=50, choices=[('Ale', (('wheat ale', 'Wheat Ale'),)), ('Lager', ('generic lager', 'Generic Lager'))]),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='type',
            field=models.CharField(max_length=50, choices=[('ale', 'Ale'), ('lager', 'Lager')]),
        ),
    ]
