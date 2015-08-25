# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0016_auto_20150723_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
