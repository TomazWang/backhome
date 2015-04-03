# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0016_auto_20150403_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='generation',
            field=models.IntegerField(default=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='seniority',
            field=models.IntegerField(default=9),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='password',
            field=models.CharField(blank=True, max_length=100),
            preserve_default=True,
        ),
    ]
