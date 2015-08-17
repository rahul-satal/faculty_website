# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_auto_20150817_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='about_desc',
            field=models.TextField(max_length=5000, verbose_name='Description'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myfriend',
            name='name',
            field=models.CharField(unique=True, max_length=200),
            preserve_default=True,
        ),
    ]
