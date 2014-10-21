# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_auto_20141021_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='malt',
            name='amount',
            field=models.DecimalField(decimal_places=3, max_digits=10, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='malt',
            name='name',
            field=models.CharField(max_length=50, default='malt'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='yeast',
            name='amount',
            field=models.DecimalField(decimal_places=3, max_digits=10, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='yeast',
            name='name',
            field=models.CharField(max_length=50, default='yeast'),
            preserve_default=False,
        ),
    ]
