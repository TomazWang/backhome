# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0017_auto_20150403_1306'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ['group', 'generation', 'seniority', '-gender']},
        ),
    ]
