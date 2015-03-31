# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_auto_20150330_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decision',
            name='decision',
            field=models.CharField(choices=[('NS', 'NOT_SURE'), ('YES', 'YES'), ('NDY', 'NOT_DECIDED_YET'), ('NO', 'NO')], default='NDY', max_length=5),
            preserve_default=True,
        ),
    ]
