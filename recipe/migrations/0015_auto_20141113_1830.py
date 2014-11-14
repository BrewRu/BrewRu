# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0014_auto_20141105_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='subtype',
            field=models.CharField(choices=[('Ale', (('pale ale', 'Pale Ale'), ('ipa', 'IPA'), ('amber', 'Amber'), ('brown', 'Brown'), ('wheat ale', 'Wheat Ale'), ('stout', 'Stout'), ('belgian', 'Belgian'))), ('Lager', (('light lager', 'Light Lager'), ('hybrid lager', 'Hybrid Lager'), ('bock', 'Bock')))], max_length=50, default='wheat ale'),
            preserve_default=True,
        ),
    ]
