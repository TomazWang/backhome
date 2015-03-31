# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0011_auto_20150331_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decision',
            name='decision',
            field=models.CharField(choices=[('NDY', 'NOT_DECIDED_YET'), ('YES', 'YES'), ('NO', 'NO'), ('NS', 'NOT_SURE')], max_length=5, default='NDY'),
            preserve_default=True,
        ),
    ]
