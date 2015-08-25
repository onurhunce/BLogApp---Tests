# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0026_auto_20150817_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=stdimage.models.StdImageField(null=True, upload_to=b'images/', blank=True),
        ),
    ]
