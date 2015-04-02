# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0015_auto_20150402_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decision',
            name='decision',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes'), (2, 'Later')], default=0),
            preserve_default=True,
        ),
    ]
