# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Decision',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('decision', models.CharField(choices=[('NO', 'NO'), ('NS', 'NOT_SURE'), ('YES', 'YES'), ('NDY', 'NOT_DECIDED_YET')], default='NDY', max_length=5)),
                ('member', models.ForeignKey(to='page.Member', related_name='decisions')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='member',
            name='password',
            field=models.CharField(default='someCode', max_length=100),
            preserve_default=False,
        ),
    ]
