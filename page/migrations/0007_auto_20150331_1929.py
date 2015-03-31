# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0006_auto_20150331_1924'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['generation', 'seniority']},
        ),
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ['generation', 'gender']},
        ),
        migrations.AlterField(
            model_name='decision',
            name='decision',
            field=models.CharField(choices=[('NDY', 'NOT_DECIDED_YET'), ('NO', 'NO'), ('YES', 'YES'), ('NS', 'NOT_SURE')], max_length=5, default='NDY'),
            preserve_default=True,
        ),
    ]
