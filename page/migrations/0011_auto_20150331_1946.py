# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0010_auto_20150331_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decision',
            name='decision',
            field=models.CharField(default='NDY', max_length=5, choices=[('YES', 'YES'), ('NS', 'NOT_SURE'), ('NO', 'NO'), ('NDY', 'NOT_DECIDED_YET')]),
            preserve_default=True,
        ),
    ]
