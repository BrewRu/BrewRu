# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0007_remove_malt_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yeast',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='yeast',
            name='pitchrate',
        ),
        migrations.AddField(
            model_name='recipe',
            name='yeast_pitch_rate',
            field=models.DecimalField(decimal_places=3, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
