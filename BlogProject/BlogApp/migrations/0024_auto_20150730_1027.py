# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0023_auto_20150730_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='added_friend',
            field=models.ForeignKey(blank=True, to='BlogApp.UserProfile', null=True),
        ),
        migrations.AlterField(
            model_name='friend',
            name='friend',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
