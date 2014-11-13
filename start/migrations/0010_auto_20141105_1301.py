# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0009_hopsil_maltil_yeastil'),
    ]

    operations = [
        migrations.AddField(
            model_name='hopsil',
            name='recipe',
            field=models.ForeignKey(default=1, to='recipe.Recipe'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maltil',
            name='recipe',
            field=models.ForeignKey(default=1, to='recipe.Recipe'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='yeastil',
            name='recipe',
            field=models.ForeignKey(default=1, to='recipe.Recipe'),
            preserve_default=False,
        ),
    ]
