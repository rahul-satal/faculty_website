# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20150817_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='example',
            name='name',
            field=models.CharField(default='Rahul', max_length=25),
            preserve_default=True,
        ),
    ]
