# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0017_auto_20150723_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=stdimage.models.StdImageField(upload_to=b'images/profile', blank=True),
        ),
    ]
