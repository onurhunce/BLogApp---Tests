# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0014_auto_20150716_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=stdimage.models.StdImageField(upload_to=b'images/', blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_mail',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
