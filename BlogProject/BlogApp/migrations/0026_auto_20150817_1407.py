# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0025_auto_20150813_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime.now, null=True, verbose_name=b'date published', blank=True),
        ),
    ]
