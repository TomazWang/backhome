# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_auto_20150331_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decision',
            name='decision',
            field=models.CharField(max_length=5, default='NDY', choices=[('NDY', 'NOT_DECIDED_YET'), ('NS', 'NOT_SURE'), ('NO', 'NO'), ('YES', 'YES')]),
            preserve_default=True,
        ),
    ]
