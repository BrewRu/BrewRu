# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_auto_20141021_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='subtype',
            field=models.CharField(choices=[('Ale', (('wheat ale', 'Wheat Ale'),)), ('Lager', ('generic lager', 'Generic Lager'))], max_length=50, default='wheat ale'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='type',
            field=models.CharField(choices=[('ale', 'Ale'), ('lager', 'Lager')], max_length=50, default='ale'),
        ),
    ]
