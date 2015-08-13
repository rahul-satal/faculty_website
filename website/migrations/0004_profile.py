# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_acadact_enclosures_geninfo_image_orie_teachapb_teachbpe_teachclmi_teachcpc_teachecfa_teachedap_teach'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('faculty_pic', models.ImageField(upload_to='Images/Pic')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
