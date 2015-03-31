# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_auto_20150331_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='gender',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='generation',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='decision',
            name='decision',
            field=models.CharField(default='NDY', choices=[('YES', 'YES'), ('NDY', 'NOT_DECIDED_YET'), ('NS', 'NOT_SURE'), ('NO', 'NO')], max_length=5),
            preserve_default=True,
        ),
    ]
