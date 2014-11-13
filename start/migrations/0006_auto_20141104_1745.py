# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0005_auto_20141021_1324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hops',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='hops',
            name='recipe',
        ),
        migrations.RemoveField(
            model_name='malt',
            name='recipe',
        ),
        migrations.RemoveField(
            model_name='yeast',
            name='recipe',
        ),
        migrations.AddField(
            model_name='hops',
            name='AAU',
            field=models.DecimalField(max_digits=10, default=1, decimal_places=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='malt',
            name='color',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='malt',
            name='country',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='malt',
            name='gravity',
            field=models.DecimalField(max_digits=10, default=1, decimal_places=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='yeast',
            name='attenuation',
            field=models.DecimalField(max_digits=10, default=1, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='yeast',
            name='flocculation',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='yeast',
            name='pitchrate',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='yeast',
            name='temp',
            field=models.DecimalField(max_digits=10, default=1, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='yeast',
            name='tolerance',
            field=models.DecimalField(max_digits=10, default=1, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='subtype',
            field=models.CharField(choices=[('Ale', (('wheat ale', 'Wheat Ale'),)), ('Lager', (('generic lager', 'Bock'),))], default='wheat ale', max_length=50),
            preserve_default=True,
        ),
    ]
