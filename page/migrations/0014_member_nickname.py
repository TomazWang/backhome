# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0013_auto_20150331_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='nickName',
            field=models.CharField(max_length=10, default='家人'),
            preserve_default=False,
        ),
    ]
