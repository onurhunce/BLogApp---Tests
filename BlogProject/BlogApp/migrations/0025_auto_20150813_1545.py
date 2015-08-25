# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0024_auto_20150730_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='added_friend',
            field=models.ForeignKey(related_name='added_friend', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='friend',
            name='friend',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='friend',
            name='friendship_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'friend_date', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='friend',
            unique_together=set([('added_friend', 'friend')]),
        ),
    ]
