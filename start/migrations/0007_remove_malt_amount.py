# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0006_auto_20141104_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='malt',
            name='amount',
        ),
    ]
