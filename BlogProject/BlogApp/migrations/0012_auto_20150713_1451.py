# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0011_auto_20150713_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_mail',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_name',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
