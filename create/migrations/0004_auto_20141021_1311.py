# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_auto_20141021_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='hops',
            name='amount',
            field=models.DecimalField(max_digits=10, decimal_places=3, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hops',
            name='country',
            field=models.CharField(max_length=50, default='United States'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hops',
            name='name',
            field=models.CharField(max_length=50, default='Hops'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='yeast',
            name='manufacturer',
            field=models.CharField(max_length=50, default='Hops'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='subtype',
            field=models.CharField(max_length=50, choices=[('Ale', (('wheat ale', 'Wheat Ale'),)), ('Lager', (('generic lager', 'Generic Lager'),))], default='wheat ale'),
        ),
    ]
