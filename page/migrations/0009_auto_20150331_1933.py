# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0008_auto_20150331_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='seniority',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='decision',
            name='decision',
            field=models.CharField(default='NDY', max_length=5, choices=[('NS', 'NOT_SURE'), ('NDY', 'NOT_DECIDED_YET'), ('YES', 'YES'), ('NO', 'NO')]),
            preserve_default=True,
        ),
    ]
