# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0008_auto_20150708_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='slug_name',
            field=models.SlugField(default=datetime.datetime(2015, 7, 10, 7, 15, 17, 950542, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(max_length=200),
        ),
    ]
