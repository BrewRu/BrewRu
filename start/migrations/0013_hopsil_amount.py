# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0012_remove_maltil_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='hopsil',
            name='amount',
            field=models.DecimalField(default=1, decimal_places=2, max_digits=10),
            preserve_default=False,
        ),
    ]
