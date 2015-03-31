# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_auto_20150331_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='generation',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='seniority',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='decision',
            name='decision',
            field=models.CharField(choices=[('NDY', 'NOT_DECIDED_YET'), ('NS', 'NOT_SURE'), ('YES', 'YES'), ('NO', 'NO')], default='NDY', max_length=5),
            preserve_default=True,
        ),
    ]
