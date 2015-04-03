# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0018_auto_20150403_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='nickName',
            field=models.CharField(max_length=10, blank=True),
            preserve_default=True,
        ),
    ]
