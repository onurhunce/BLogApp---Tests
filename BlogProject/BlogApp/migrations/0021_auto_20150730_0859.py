# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0020_auto_20150729_1656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='friend_list',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='friend_list',
            field=models.ForeignKey(blank=True, to='BlogApp.Friend', null=True),
        ),
    ]
