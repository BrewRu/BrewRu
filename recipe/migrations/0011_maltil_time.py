# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0010_auto_20141105_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='maltil',
            name='time',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
