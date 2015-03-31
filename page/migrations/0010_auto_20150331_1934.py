# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0009_auto_20150331_1933'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ['generation', 'seniority', '-gender']},
        ),
        migrations.AlterField(
            model_name='decision',
            name='decision',
            field=models.CharField(max_length=5, default='NDY', choices=[('NS', 'NOT_SURE'), ('NDY', 'NOT_DECIDED_YET'), ('NO', 'NO'), ('YES', 'YES')]),
            preserve_default=True,
        ),
    ]
