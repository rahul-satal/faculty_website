# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='Name', max_length=200),
            preserve_default=True,
        ),
    ]
