# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20150817_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mystudent',
            name='name',
            field=models.CharField(unique=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myteacher',
            name='name',
            field=models.CharField(unique=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='profile',
            unique_together=set([('name', 'faculty_pic')]),
        ),
    ]
