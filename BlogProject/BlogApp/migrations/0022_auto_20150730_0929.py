# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0021_auto_20150730_0859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='friends',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='friend_list',
        ),
        migrations.AddField(
            model_name='friend',
            name='friend',
            field=models.OneToOneField(null=True, blank=True, to='BlogApp.UserProfile'),
        ),
    ]
